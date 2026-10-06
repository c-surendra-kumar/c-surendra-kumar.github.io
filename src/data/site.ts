/**
 * Static site data. Everything here is copied from
 * ~/.claude/skills/job-app-tailor/resources/Surendra_Kumar_Resume.docx
 * so the site and the master resume say the same thing.
 *
 * The resume's phone number is deliberately not published here; the resume PDF
 * carries it for anyone who downloads it.
 */

export const SITE = {
  name: 'Surendra Kumar Chandrasekaran',
  shortName: 'Surendra Kumar Chandrasekaran',
  url: 'https://c-surendra-kumar.github.io',
  role: 'MS Applied Machine Learning, University of Maryland',
  tagline:
    'Driven by impact, I build AI systems that solve real-world problems reliably.',
  seeking:
    'Open to AI/ML and forward-deployed roles from mid-2027.',
  description:
    'Surendra Kumar Chandrasekaran - MS Applied Machine Learning at the University of Maryland. AI agents you can trust with real tasks, honest evaluation, and efficient training. Open to AI/ML and forward-deployed roles from mid-2027.',
  location: 'College Park, MD',
  email: 'schandr3@umd.edu',
  github: 'https://github.com/c-surendra-kumar',
  githubHandle: 'c-surendra-kumar',
  linkedin: 'https://linkedin.com/in/surendra-kumar-c',
  linkedinHandle: 'surendra-kumar-c',
  scholar:
    'https://scholar.google.com/citations?view_op=new_articles&hl=en&imq=Surendra+Kumar+Chandrasekaran',
  resumePath: '/Surendra_Kumar_C_Resume.pdf',
} as const;

/** About copy. The lead line is SITE.tagline; these follow it. */
export const ABOUT = [
  'I am a graduate student in Applied Machine Learning at the University of Maryland, College Park.',
  'I care most about what happens after the model works: how a team actually operates, whether the thing fits that workflow, and what it does when it breaks. I like being the engineer in the room with the people who have the problem: scoping it, prototyping quickly, and owning it through to production.',
];

/**
 * Current focus areas. Interests rather than delivered work, so they are
 * deliberately phrased as exploration and carry no metrics.
 */
export const FOCUS = [
  {
    label: 'Agentic and language-centric AI',
    detail:
      'autonomous agents that plan, reason, and use external tools; RAG pipelines combining embeddings, vector search, and generative reasoning into knowledge-grounded systems; LLM fine-tuning and adaptation for alignment and efficiency.',
  },
  {
    label: 'Multimodal and vision-language systems',
    detail:
      'integrating text, images, and audio into unified representations, and the cross-modal evaluation that tells you whether they actually work.',
  },
  {
    label: 'Data and systems engineering',
    detail:
      'scalable pipelines, dataset preparation, and deployment-ready infrastructure for training and serving large models, so research advances turn into something production-ready.',
  },
];

/** Availability, stated after the focus list. */
export const AVAILABILITY =
  'I am open to AI/ML and forward-deployed engineering roles from mid-2027.';

/** Closing line, rendered with the email linked. */
export const ABOUT_CLOSER = {
  before: "If you are building AI that has to earn its place in people's lives, ",
  link: 'I would love to connect',
  after: '.',
};

export const SKILLS: { label: string; items: string[] }[] = [
  { label: 'Languages', items: ['Python', 'C/C++', 'Java', 'SQL', 'JAX'] },
  {
    label: 'ML/AI',
    items: [
      'PyTorch',
      'HuggingFace',
      'scikit-learn',
      'Transformers',
      'NLP',
      'Computer Vision',
      'RAG',
      'Model Optimization',
    ],
  },
  {
    label: 'LLM/Agents',
    items: [
      'LangGraph',
      'LangChain',
      'LlamaIndex',
      'MCP',
      'Agentic Workflows',
      'Tool Calling',
      'Prompt Engineering',
    ],
  },
  {
    label: 'Engineering',
    items: ['FastAPI', 'Docker', 'AWS', 'GCP', 'Linux', 'Git', 'Redis'],
  },
  {
    label: 'Data',
    items: ['PostgreSQL', 'MySQL', 'MongoDB', 'FAISS', 'PySpark', 'NumPy', 'Pandas'],
  },
];

export const EDUCATION = [
  {
    degree: 'M.S. in Applied Machine Learning',
    school: 'University of Maryland, College Park',
    dates: 'Sep 2025 - May 2027',
    gpa: '4.0 / 4.0',
    coursework: [
      'Principles of Machine Learning',
      'Data Science',
      'Probability and Statistics',
      'Introduction to Optimization',
      'Generative AI Agents',
      'Data Structures for Machine Learning',
    ],
  },
  {
    degree: 'B.E. in Computer Science and Engineering',
    school: 'College of Engineering, Guindy (Anna University)',
    dates: 'Nov 2021 - May 2025',
    gpa: '3.7 / 4.0',
    coursework: [
      'Data Structures and Algorithms',
      'Computer Architecture',
      'Operating Systems',
      'DBMS',
    ],
  },
];

/**
 * Shown in a carousel: the photo fills the slide and this text is overlaid on
 * it, so keep the list short and each entry substantial. `image` is the
 * filename under src/assets/; Carousel resolves it at build time.
 */
export const AWARDS = [
  {
    title: 'Excellence in Entrepreneurship',
    slug: 'excellence-entrepreneurship',
    mark: 'ee',
    date: '2025',
    event: 'Global Business Conclave 2025',
    image: 'excellence_in_entrepreneurship.jpg',
    detail:
      'Awarded personally for entrepreneurial work as founding engineer at EyeZenX, a clinician-built diagnostic platform. Shortlisted from a large pool of startups through multiple jury rounds and an on-stage pitch. EyeZenX was named HealthTech Startup of the Year at the same event.',
  },
  {
    title: 'Gemini Hack Night - 1st place',
    slug: 'gemini-hack-night',
    mark: 'gh',
    date: 'Nov 2025',
    event: 'Also won Best Healthcare and Wellness Hack',
    image: 'hackathon.jpg',
    detail:
      'Built Lifeguard AI with a two-person team: a CPR assistant giving real-time audio and visual feedback during chest compressions. Prototyped pose detection with Gemini, then moved to MediaPipe Pose for higher-fidelity real-time landmark tracking, and shipped a deployed web app inside the 5-hour event. 1st among 150+ participants, at 92% measurement accuracy.',
  },
];

export const CERTIFICATIONS = [
  {
    title: 'Claude Certified Architect - Foundations',
    slug: 'claude-architect',
    mark: 'cc',
    date: 'Jul 2026',
    issuer: 'Anthropic',
    detail:
      'Validated expertise in Agentic Architecture, MCP Tool Design, Context Engineering, Structured-Output Generation and Claude Code configuration for Production-Grade Claude Deployments.',
  },
  {
    title: 'Machine Learning Specialization',
    slug: 'ml-specialization',
    mark: 'ml',
    date: '',
    issuer: 'DeepLearning.AI and Stanford Online (Andrew Ng)',
    detail:
      'Three-course specialization covering supervised learning, advanced learning algorithms, and unsupervised learning with recommenders and reinforcement learning.',
  },
];

/**
 * Top bar. The section entries are root-relative anchors so they also work
 * from /blog/ and /resume/: the browser loads home, then jumps to the section.
 * `spy` marks the ones the scroll spy should highlight while on the home page.
 */
export const NAV_LINKS = [
  { href: '/', label: 'About', spy: null },
  { href: '/#work', label: 'Work', spy: 'work' },
  { href: '/#projects', label: 'Projects', spy: 'projects' },
  { href: '/#publications', label: 'Publications', spy: 'publications' },
  { href: '/#skills', label: 'Tech Stack', spy: 'skills' },
  { href: '/blog/', label: 'Blog', spy: null },
  { href: '/resume/', label: 'Resume', spy: null },
];

/** The full in-page index, in the sidebar. Superset of the top bar. */
export const SECTION_LINKS = [
  { href: '#work', label: 'Work' },
  { href: '#projects', label: 'Projects' },
  { href: '#publications', label: 'Publications' },
  { href: '#skills', label: 'Tech Stack' },
  { href: '#education', label: 'Education' },
  { href: '#certifications', label: 'Certifications' },
  { href: '#awards', label: 'Awards' },
];

/** Research interests shown in the sidebar. Descriptive, not claims. */
export const INTERESTS = [
  'NLP',
  'Agentic AI',
  'RAG',
  'LLMs',
  'Multimodal ML',
  'Political NLP',
  'LLM Evaluation',
  'Efficient Training',
];

/**
 * The same 34 tools as SKILLS, re-cut as the layers of a system rather than as
 * resume categories. A grouped list says "here are words I know"; a stack says
 * "I can build the whole thing end to end", which is the actual pitch.
 *
 * Every entry in SKILLS must appear here exactly once - SkillStack asserts it
 * at build time, so a tool added to the resume cannot silently vanish here.
 */
export const STACK_LAYERS: {
  label: string;
  caption: string;
  items: string[];
}[] = [
  {
    label: 'Orchestration',
    caption: 'how the system decides what to do next',
    items: [
      'LangGraph',
      'LangChain',
      'LlamaIndex',
      'MCP',
      'Agentic Workflows',
      'Tool Calling',
      'Prompt Engineering',
    ],
  },
  {
    label: 'Models',
    caption: 'what actually does the reasoning',
    items: [
      'PyTorch',
      'HuggingFace',
      'Transformers',
      'scikit-learn',
      'NLP',
      'Computer Vision',
      'Model Optimization',
      'JAX',
    ],
  },
  {
    label: 'Retrieval & memory',
    caption: 'what the system knows, and where it looks',
    items: ['RAG', 'FAISS', 'PostgreSQL', 'MySQL', 'MongoDB', 'Redis'],
  },
  {
    label: 'Data',
    caption: 'getting the corpus into a usable shape',
    items: ['PySpark', 'NumPy', 'Pandas', 'SQL'],
  },
  {
    label: 'Serving & runtime',
    caption: 'how it reaches a person',
    items: ['FastAPI', 'Docker', 'AWS', 'GCP', 'Linux', 'Git'],
  },
  {
    label: 'Foundations',
    caption: 'the floor the rest of it sits on',
    items: ['Python', 'C/C++', 'Java'],
  },
];
