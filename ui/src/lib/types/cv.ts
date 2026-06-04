export interface PersonalInfo {
	name: string;
	surname: string;
	address: string;
	birthday?: string;
	email?: string;
	phone: string;
	github: string;
	linkedin: string;
	nationality: string;
	photo_url: string;
}

export interface Experience {
	job_title: string;
	company: string;
	company_type: string;
	start_date?: string;
	end_date?: string;
	description: string;
}

export interface Education {
	degree: string;
	institution: string;
	graduation_year?: number;
}

export interface TechSkill {
	name: string;
	level: string;
}

export interface SoftSkill {
	name: string;
}

export interface LangSkill {
	lang: string;
	overall_lvl: string;
}

export interface Certification {
	title: string;
	issuer: string;
	year?: number;
	url: string;
}

export interface Publication {
	title: string;
	venue: string;
	year?: number;
	url: string;
}

export interface CVProfile {
	id: string;
	label: string;
	personal_info: PersonalInfo;
	experience: Experience[];
	education: Education[];
	tech_skills: TechSkill[];
	soft_skills: SoftSkill[];
	lang_skills: LangSkill[];
	certifications: Certification[];
	publications: Publication[];
}

export interface CVProfileSummary {
	id: string;
	label: string;
	name: string;
	surname: string;
}

export interface CreateCVProfile {
	label: string;
	personal_info?: Partial<PersonalInfo>;
	experience?: Experience[];
	education?: Education[];
	tech_skills?: TechSkill[];
	soft_skills?: SoftSkill[];
	lang_skills?: LangSkill[];
	certifications?: Certification[];
	publications?: Publication[];
}

export function emptyPersonalInfo(): PersonalInfo {
	return { name: '', surname: '', address: '', phone: '', github: '', linkedin: '', nationality: '', photo_url: '' };
}
