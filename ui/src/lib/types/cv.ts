// ─── Core types ──────────────────────────────────────────────────────────────
// Aligned with the Python Pydantic model (app/model.py) and extended to cover
// all fields used by the LaTeX templates (moderncv, europass).

export interface PersonalInfo {
  name: string;
  surname: string;
  job_title: string; // professional title shown below name
  email: string;
  phone: string;
  address: string;
  birthday: string; // ISO date YYYY-MM-DD
  gender: string;
  nationality: string;
  tax_code: string;
  github: string;
  linkedin: string;
  url_pic: string;
}

export interface Experience {
  job_title: string;
  company: string;
  company_type: string;
  start_date: string; // ISO date
  end_date: string | null; // null = present
  description: string;
  achievements: string[];
}

export interface Education {
  degree: string;
  institution: string;
  start_date: string; // ISO date (optional, empty string if unknown)
  graduation_year: number;
  grade: string;
}

export interface TechSkill {
  degree: string;
  level: number; // 1–5
  years: number;
}

export interface SoftSkill {
  degree: string;
}

export interface LangSkill {
  lang: string;
  overall_lvl: string;
  speaking_lvl: string;
  writing_lvl: string;
  listening_lvl: string;
  comprehension_level: string;
}

export interface DrivingSkill {
  driving_license: string;
}

export interface Skills {
  tech_skills: TechSkill[];
  soft_skills: SoftSkill[];
  lang_skills: LangSkill[];
  driving_skills: DrivingSkill[];
}

export interface Certification {
  title: string;
  released_at: string;
}

export interface Publication {
  authors: string;
  title: string;
  journal: string;
  details: string;
}

export interface Letter {
  is_active: boolean;
  company: {
    name: string;
    address: string;
    city: string;
  };
  content: string;
}

export interface Options {
  cvlanguage: string; // 'en' | 'it' | ...
}

export interface CVData {
  code: string; // output file identifier (e.g. "mycv" → cv-mycv.pdf)
  personal_info: PersonalInfo;
  experience: Experience[];
  education: Education[];
  skills: Skills;
  certifications: Certification[];
  publications: Publication[];
  letter: Letter;
  options: Options;
}

// ─── Factories ───────────────────────────────────────────────────────────────

export function emptyExperience(): Experience {
  return {
    job_title: '',
    company: '',
    company_type: '',
    start_date: '',
    end_date: null,
    description: '',
    achievements: [],
  };
}

export function emptyEducation(): Education {
  return {
    degree: '',
    institution: '',
    start_date: '',
    graduation_year: new Date().getFullYear(),
    grade: '',
  };
}

export function emptyTechSkill(): TechSkill {
  return { degree: '', level: 3, years: 1 };
}

export function emptySoftSkill(): SoftSkill {
  return { degree: '' };
}

export function emptyLangSkill(): LangSkill {
  return {
    lang: '',
    overall_lvl: '',
    speaking_lvl: '',
    writing_lvl: '',
    listening_lvl: '',
    comprehension_level: '',
  };
}

export function emptyDrivingSkill(): DrivingSkill {
  return { driving_license: '' };
}

export function emptyCertification(): Certification {
  return { title: '', released_at: '' };
}

export function emptyPublication(): Publication {
  return { authors: '', title: '', journal: '', details: '' };
}

// ─── Default ─────────────────────────────────────────────────────────────────

export const DEFAULT_CV_DATA: CVData = {
  code: 'mycv',
  personal_info: {
    name: '',
    surname: '',
    job_title: '',
    email: '',
    phone: '',
    address: '',
    birthday: '',
    gender: '',
    nationality: '',
    tax_code: '',
    github: '',
    linkedin: '',
    url_pic: '',
  },
  experience: [],
  education: [],
  skills: {
    tech_skills: [],
    soft_skills: [],
    lang_skills: [],
    driving_skills: [],
  },
  certifications: [],
  publications: [],
  letter: {
    is_active: false,
    company: { name: '', address: '', city: '' },
    content: '',
  },
  options: { cvlanguage: 'en' },
};
