import os, re, sqlite3
from pathlib import Path
from datetime import datetime
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, flash, session, abort, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from pypdf import PdfReader
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

ROOT=Path(__file__).resolve().parent
UPLOADS=ROOT/"uploads"; UPLOADS.mkdir(exist_ok=True)
DB=ROOT/"hirelens.db"; MAX_MB=5
app=Flask(__name__); app.secret_key=os.environ.get("FLASK_SECRET_KEY","change-this-development-key")
app.config["MAX_CONTENT_LENGTH"]=MAX_MB*1024*1024
SKILLS=["python","java","c++","c","javascript","html","css","flask","django","sql","mysql","sqlite","mongodb","machine learning","deep learning","artificial intelligence","data analysis","pandas","numpy","scikit-learn","tensorflow","pytorch","nlp","git","github","rest api","aws","azure","docker","linux","excel","communication","problem solving","data structures","algorithms","react","node.js","php","power bi","tableau","statistics"]

def conn():
 c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; c.execute("PRAGMA foreign_keys=ON"); return c
def stamp(): return datetime.now().strftime("%Y-%m-%d %H:%M")
def init():
 with conn() as c:
  c.executescript("""
  CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT NOT NULL,email TEXT UNIQUE NOT NULL,password_hash TEXT NOT NULL,role TEXT NOT NULL CHECK(role IN('admin','candidate')),created_at TEXT NOT NULL);
  CREATE TABLE IF NOT EXISTS jobs(id INTEGER PRIMARY KEY,admin_id INTEGER NOT NULL,title TEXT NOT NULL,department TEXT,location TEXT,job_type TEXT,description TEXT NOT NULL,required_skills TEXT NOT NULL,status TEXT NOT NULL DEFAULT 'Open',created_at TEXT NOT NULL,FOREIGN KEY(admin_id) REFERENCES users(id));
  CREATE TABLE IF NOT EXISTS applications(id INTEGER PRIMARY KEY,job_id INTEGER NOT NULL,candidate_id INTEGER NOT NULL,resume_filename TEXT NOT NULL,resume_path TEXT NOT NULL,resume_text TEXT NOT NULL,extracted_skills TEXT NOT NULL,skill_coverage REAL NOT NULL,text_similarity REAL NOT NULL,overall_score REAL NOT NULL,status TEXT NOT NULL DEFAULT 'Applied',applied_at TEXT NOT NULL,UNIQUE(job_id,candidate_id),FOREIGN KEY(job_id) REFERENCES jobs(id),FOREIGN KEY(candidate_id) REFERENCES users(id));
  """)
def login_required(role=None):
 def deco(fn):
  @wraps(fn)
  def wrapper(*a,**kw):
   if not session.get("user_id"): flash("Please log in first.","warning"); return redirect(url_for("login"))
   if role and session.get("role")!=role: abort(403)
   return fn(*a,**kw)
  return wrapper
 return deco
def get_user():
 if not session.get("user_id"): return None
 with conn() as c: return c.execute("SELECT id,name,email,role FROM users WHERE id=?",(session["user_id"],)).fetchone()
@app.context_processor
def globals_for_templates(): return {"current_user":get_user(),"project_name":"AI Resume Screening & Candidate Ranking System"}
def ext_ok(name): return "." in name and name.rsplit(".",1)[1].lower() in {"pdf","docx"}
def valid_email(email):
 return bool(re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email))
def valid_person_name(name):
 return bool(name and len(name) <= 80 and re.fullmatch(r"[A-Za-z][A-Za-z .'-]*", name))
def validate_job_fields(vals):
 title, department, location, job_type, description, skills = vals
 if not title or len(title) > 100: return "Job title is required and must be within 100 characters."
 if len(department) > 80: return "Department must be within 80 characters."
 if len(location) > 100: return "Location must be within 100 characters."
 if job_type not in {"Full-time", "Part-time", "Internship", "Contract"}: return "Select a valid job type."
 if len(description.strip()) < 20 or len(description) > 5000: return "Description must contain 20 to 5000 characters."
 if not skills or len(skills) > 1000: return "Required skills are mandatory and must be within 1000 characters."
 if not any(item.strip() for item in skills.split(",")): return "Enter at least one required skill."
 return None
def read_resume(path):
 if Path(path).suffix.lower()==".pdf": return "\n".join(p.extract_text() or "" for p in PdfReader(path).pages).strip()
 if Path(path).suffix.lower()==".docx": return "\n".join(p.text for p in Document(path).paragraphs).strip()
 return ""
def skills_in(text):
 text=(text or "").lower(); found=[]
 for s in SKILLS:
  if re.search(r"(?<![a-z0-9])"+re.escape(s)+r"(?![a-z0-9])",text): found.append(s)
 return sorted(set(found))
def analyze(text,job):
 required=sorted(set(s.strip().lower() for s in job["required_skills"].split(",") if s.strip()))
 found=skills_in(text); matched=sorted(set(required)&set(found)); missing=sorted(set(required)-set(found))
 coverage=100*len(matched)/len(required) if required else 0
 try:
  m=TfidfVectorizer(stop_words="english").fit_transform([job["title"]+" "+job["description"]+" "+job["required_skills"],text])
  similarity=float(cosine_similarity(m[0:1],m[1:2])[0][0]*100)
 except ValueError: similarity=0
 overall=min(100,max(0,coverage*.6+similarity*.4))
 return {"skills":found,"matched":matched,"missing":missing,"coverage":round(coverage,2),"similarity":round(similarity,2),"overall":round(overall,2)}
@app.route("/")
def home():
 if session.get("role")=="admin": return redirect(url_for("admin"))
 if session.get("role")=="candidate": return redirect(url_for("candidate"))
 with conn() as c: jobs=c.execute("SELECT * FROM jobs WHERE status='Open' ORDER BY id DESC LIMIT 6").fetchall()
 return render_template("home.html",jobs=jobs)
@app.route("/register",methods=["GET","POST"])
def register():
 if request.method=="POST":
  name=request.form.get("name","").strip(); email=request.form.get("email","").strip().lower(); pw=request.form.get("password","")
  if not valid_person_name(name): flash("Enter a valid name (letters, spaces, apostrophes, dots or hyphens; maximum 80 characters).","danger")
  elif not valid_email(email): flash("Enter a valid email address.","danger")
  elif len(pw)<8 or len(pw)>128: flash("Password must contain 8 to 128 characters.","danger")
  else:
   try:
    with conn() as c: c.execute("INSERT INTO users(name,email,password_hash,role,created_at) VALUES(?,?,?,?,?)",(name,email,generate_password_hash(pw),"candidate",stamp())); c.commit()
    flash("Account created. Please log in.","success"); return redirect(url_for("login"))
   except sqlite3.IntegrityError: flash("That email is already registered.","danger")
 return render_template("register.html")
@app.route("/login",methods=["GET","POST"])
def login():
 if request.method=="POST":
  with conn() as c: u=c.execute("SELECT * FROM users WHERE email=?",(request.form.get("email","").strip().lower(),)).fetchone()
  if u and check_password_hash(u["password_hash"],request.form.get("password","")):
   session.clear(); session.update(user_id=u["id"],role=u["role"],name=u["name"])
   return redirect(url_for("admin" if u["role"]=="admin" else "candidate"))
  flash("Email or password is incorrect.","danger")
 return render_template("login.html")
@app.route("/logout")
def logout(): session.clear(); return redirect(url_for("home"))
@app.route("/admin")
@login_required("admin")
def admin():
 with conn() as c:
  jobs=c.execute("SELECT j.*,COUNT(a.id) applicants FROM jobs j LEFT JOIN applications a ON a.job_id=j.id WHERE j.admin_id=? GROUP BY j.id ORDER BY j.id DESC",(session["user_id"],)).fetchall()
  total=c.execute("SELECT COUNT(*) FROM applications a JOIN jobs j ON j.id=a.job_id WHERE j.admin_id=?",(session["user_id"],)).fetchone()[0]
  statuses=c.execute("SELECT a.status,COUNT(*) n FROM applications a JOIN jobs j ON j.id=a.job_id WHERE j.admin_id=? GROUP BY a.status",(session["user_id"],)).fetchall()
 return render_template("admin.html",jobs=jobs,total=total,statuses=statuses)
@app.route("/admin/jobs/new",methods=["GET","POST"])
@login_required("admin")
def job_new():
 if request.method=="POST":
  vals=[request.form.get(k,"").strip() for k in ["title","department","location","job_type","description","required_skills"]]
  error=validate_job_fields(vals)
  status_value=request.form.get("status","Open")
  if status_value not in {"Open", "Closed"}: error="Select a valid vacancy status."
  if error: flash(error,"danger")
  else:
   with conn() as c: c.execute("INSERT INTO jobs(admin_id,title,department,location,job_type,description,required_skills,status,created_at) VALUES(?,?,?,?,?,?,?,?,?)",(session["user_id"],*vals,status_value,stamp())); c.commit()
   flash("Vacancy saved.","success"); return redirect(url_for("admin"))
 return render_template("job_form.html",job=None)
@app.route("/admin/jobs/<int:j_id>/edit",methods=["GET","POST"])
@login_required("admin")
def job_edit(j_id):
 with conn() as c:
  job=c.execute("SELECT * FROM jobs WHERE id=? AND admin_id=?",(j_id,session["user_id"])).fetchone()
  if not job: abort(404)
  if request.method=="POST":
   vals=[request.form.get(k,"").strip() for k in ["title","department","location","job_type","description","required_skills"]]
   error=validate_job_fields(vals)
   status_value=request.form.get("status","Open")
   if status_value not in {"Open", "Closed"}: error="Select a valid vacancy status."
   if error: flash(error,"danger")
   else:
    c.execute("UPDATE jobs SET title=?,department=?,location=?,job_type=?,description=?,required_skills=?,status=? WHERE id=?",(*vals,status_value,j_id)); c.commit(); flash("Vacancy updated.","success"); return redirect(url_for("admin"))
 return render_template("job_form.html",job=job)
@app.route("/jobs")
@login_required()
def jobs():
 q=request.args.get("q","").strip(); loc=request.args.get("location","").strip()
 sql="SELECT * FROM jobs WHERE status='Open'"; args=[]
 if q: sql+=" AND (title LIKE ? OR description LIKE ? OR required_skills LIKE ?)"; args += [f"%{q}%"]*3
 if loc: sql+=" AND location LIKE ?"; args.append(f"%{loc}%")
 with conn() as c:
  rows=c.execute(sql+" ORDER BY id DESC",args).fetchall()
  applied={r["job_id"] for r in c.execute("SELECT job_id FROM applications WHERE candidate_id=?",(session["user_id"],)).fetchall()} if session["role"]=="candidate" else set()
 return render_template("jobs.html",jobs=rows,applied=applied,q=q,location=loc)
@app.route("/jobs/<int:j_id>")
@login_required()
def job_detail(j_id):
 with conn() as c:
  job=c.execute("SELECT * FROM jobs WHERE id=?",(j_id,)).fetchone()
  if not job: abort(404)
  application=c.execute("SELECT * FROM applications WHERE job_id=? AND candidate_id=?",(j_id,session["user_id"])).fetchone() if session["role"]=="candidate" else None
 return render_template("job_detail.html",job=job,application=application)
@app.route("/jobs/<int:j_id>/apply",methods=["POST"])
@login_required("candidate")
def apply(j_id):
 with conn() as c:
  job=c.execute("SELECT * FROM jobs WHERE id=? AND status='Open'",(j_id,)).fetchone()
  if not job: flash("Vacancy is closed or unavailable.","danger"); return redirect(url_for("jobs"))
  if c.execute("SELECT id FROM applications WHERE job_id=? AND candidate_id=?",(j_id,session["user_id"])).fetchone(): flash("You already applied to this vacancy.","warning"); return redirect(url_for("job_detail",j_id=j_id))
  f=request.files.get("resume")
  if not f or not f.filename or not ext_ok(f.filename): flash("Upload a valid PDF or DOCX resume.","danger"); return redirect(url_for("job_detail",j_id=j_id))
  if f.content_length == 0: flash("The selected resume file is empty.","danger"); return redirect(url_for("job_detail",j_id=j_id))
  original=secure_filename(f.filename); saved=f"u{session['user_id']}_j{j_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}_{original}"; path=UPLOADS/saved; f.save(path)
  try:
   text=read_resume(path)
   if not text: raise ValueError("No selectable text found. Scanned PDFs are not supported.")
   a=analyze(text,job)
  except Exception as e:
   path.unlink(missing_ok=True); flash("Could not read resume: "+str(e),"danger"); return redirect(url_for("job_detail",j_id=j_id))
  c.execute("INSERT INTO applications(job_id,candidate_id,resume_filename,resume_path,resume_text,extracted_skills,skill_coverage,text_similarity,overall_score,status,applied_at) VALUES(?,?,?,?,?,?,?,?,?,?,?)",(j_id,session["user_id"],original,saved,text,", ".join(a["skills"]),a["coverage"],a["similarity"],a["overall"],"Applied",stamp())); c.commit()
 flash("Application submitted successfully.","success"); return redirect(url_for("my_apps"))
@app.route("/candidate")
@login_required("candidate")
def candidate():
 with conn() as c:
  apps=c.execute("SELECT a.*,j.title,j.location FROM applications a JOIN jobs j ON j.id=a.job_id WHERE a.candidate_id=? ORDER BY a.id DESC",(session["user_id"],)).fetchall()
  recs=c.execute("SELECT * FROM jobs WHERE status='Open' AND id NOT IN(SELECT job_id FROM applications WHERE candidate_id=?) ORDER BY id DESC LIMIT 5",(session["user_id"],)).fetchall()
 return render_template("candidate.html",applications=apps,recommendations=recs)
@app.route("/applications")
@login_required("candidate")
def my_apps():
 with conn() as c: apps=c.execute("SELECT a.*,j.title,j.location,j.description,j.required_skills FROM applications a JOIN jobs j ON j.id=a.job_id WHERE a.candidate_id=? ORDER BY a.id DESC",(session["user_id"],)).fetchall()
 return render_template("my_apps.html",applications=apps)
@app.route("/applications/<int:a_id>")
@login_required()
def analysis(a_id):
 with conn() as c:
  a=c.execute("SELECT a.*,j.title,j.description,j.required_skills,j.admin_id,u.name candidate_name,u.email candidate_email FROM applications a JOIN jobs j ON j.id=a.job_id JOIN users u ON u.id=a.candidate_id WHERE a.id=?",(a_id,)).fetchone()
  if not a: abort(404)
  if session["role"]=="candidate" and a["candidate_id"]!=session["user_id"]: abort(403)
  if session["role"]=="admin" and a["admin_id"]!=session["user_id"]: abort(403)
 result=analyze(a["resume_text"],{"title":a["title"],"description":a["description"],"required_skills":a["required_skills"]})
 return render_template("analysis.html",a=a,result=result)
@app.route("/admin/jobs/<int:j_id>/applicants")
@login_required("admin")
def applicants(j_id):
 with conn() as c:
  job=c.execute("SELECT * FROM jobs WHERE id=? AND admin_id=?",(j_id,session["user_id"])).fetchone()
  if not job: abort(404)
  apps=c.execute("SELECT a.*,u.name candidate_name,u.email candidate_email FROM applications a JOIN users u ON u.id=a.candidate_id WHERE a.job_id=? ORDER BY a.overall_score DESC",(j_id,)).fetchall()
 return render_template("applicants.html",job=job,applications=apps)
@app.route("/admin/applications/<int:a_id>/status",methods=["POST"])
@login_required("admin")
def status(a_id):
 s=request.form.get("status","")
 if s not in {"Applied","Under Review","Shortlisted","Rejected","Selected"}: abort(400)
 with conn() as c:
  row=c.execute("SELECT a.id FROM applications a JOIN jobs j ON j.id=a.job_id WHERE a.id=? AND j.admin_id=?",(a_id,session["user_id"])).fetchone()
  if not row: abort(404)
  c.execute("UPDATE applications SET status=? WHERE id=?",(s,a_id)); c.commit()
 flash("Application status updated.","success"); return redirect(request.referrer or url_for("admin"))
@app.route("/admin/jobs/<int:j_id>/report")
@login_required("admin")
def report(j_id):
 with conn() as c:
  job=c.execute("SELECT * FROM jobs WHERE id=? AND admin_id=?",(j_id,session["user_id"])).fetchone()
  if not job: abort(404)
  rows=c.execute("SELECT a.*,u.name candidate_name FROM applications a JOIN users u ON u.id=a.candidate_id WHERE a.job_id=? ORDER BY a.overall_score DESC",(j_id,)).fetchall()
 path=ROOT/f"ranking_report_{j_id}.pdf"; pdf=canvas.Canvas(str(path),pagesize=letter); w,h=letter; y=h-55
 pdf.setFont("Helvetica-Bold",14); pdf.drawString(42,y,"AI Resume Screening & Candidate Ranking System"); y-=28
 pdf.setFont("Helvetica-Bold",12); pdf.drawString(42,y,("Candidate Ranking Report: "+job["title"])[:90]); y-=25
 pdf.setFont("Helvetica",9); pdf.drawString(42,y,f"Generated {stamp()} | Applicants: {len(rows)}"); y-=25
 for i,r in enumerate(rows,1):
  if y<65: pdf.showPage(); y=h-50
  pdf.drawString(42,y,f"{i}. {r['candidate_name']} | Score {r['overall_score']:.1f}% | Skills {r['skill_coverage']:.1f}% | Status {r['status']}"); y-=18
 pdf.save(); return send_file(path,as_attachment=True,download_name=f"ranking_report_{j_id}.pdf")
@app.errorhandler(403)
def forbidden(e): return render_template("error.html",code=403,message="You do not have permission to view this page."),403
@app.errorhandler(404)
def missing(e): return render_template("error.html",code=404,message="The requested page was not found."),404
@app.errorhandler(413)
def too_big(e): flash(f"File too large. Maximum size is {MAX_MB} MB.","danger"); return redirect(request.referrer or url_for("jobs"))
init()
if __name__=="__main__": app.run(debug=True)
