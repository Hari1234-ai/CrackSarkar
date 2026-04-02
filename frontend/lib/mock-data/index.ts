import { DailyPlan, UserProgressOverview, Paper } from "../../types";

export const MOCK_PROGRESS: UserProgressOverview = {
  overallCompletion: 34,
  totalTimeStudied: 1420, // minutes
  streakDays: 4,
  weakAreas: ["Indian Polity: Fundamental Rights", "Telangana Economy"],
  strongAreas: ["Indian History: Mughals", "Geography: River Systems"],
  topicWiseProgress: [
    {
      topicId: "t1",
      topicTitle: "Fundamental Rights",
      accuracy: 45,
      timeSpent: 120,
      masteryLevel: "Beginner",
      needsRevision: true,
    },
    {
      topicId: "t2",
      topicTitle: "Geography: River Systems",
      accuracy: 85,
      timeSpent: 180,
      masteryLevel: "Advanced",
      needsRevision: false,
    },
  ],
};

export const MOCK_TODAY_PLAN: DailyPlan = {
  date: new Date().toISOString(),
  overall_progress: 0,
  tasks: [
    {
      id: "tsk-1",
      type: "study",
      title: "Fundamental Rights (Polity)",
      description: "Review articles 12 to 35. Focus on exceptions.",
      duration_minutes: 45,
      completed: false,
    },
    {
      id: "tsk-2",
      type: "practice",
      title: "Geography River Systems Quiz",
      description: "Take a 20 question quiz to solidify your strong area.",
      duration_minutes: 20,
      completed: false,
    },
    {
      id: "tsk-3",
      type: "revision",
      title: "Telangana Economy",
      description: "Revisit key dates and figures from the last mock test.",
      duration_minutes: 30,
      completed: true,
    },
  ],
};

export const MOCK_SYLLABUS: Paper[] = [
  {
    id: "p1",
    exam_id: "Group_II",
    title: "Paper I: General Studies & General Abilities",
    subjects: [
      {
        id: "gs-1",
        title: "Current Affairs & Events",
        topics: [
          {
            id: "top-ca-1",
            title: "National & International Events",
            weightage: "High",
            subtopics: [
              {
                id: "subt-ca-1",
                title: "Recent International Summits",
                progress: 0,
                concepts: [
                  {
                    id: "c-ca-1",
                    title: "G20 Summit 2024",
                    content: "The 2024 G20 Rio de Janeiro summit was the nineteenth meeting of the Group of Twenty...",
                    key_points: ["Theme: Building a Just World and a Sustainable Planet", "Social inclusion and the fight against hunger"],
                    examples: ["Global Alliance against Hunger and Poverty"],
                    completed: false
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        id: "gs-2",
        title: "Science & Technology",
        topics: [
          {
            id: "top-st-1",
            title: "India's Achievements in S&T",
            weightage: "Medium",
            subtopics: [
              {
                id: "subt-st-1",
                title: "Space Research & ISRO",
                progress: 0,
                concepts: [
                  {
                    id: "c-st-1",
                    title: "Chandrayaan-3 Mission",
                    content: "Chandrayaan-3 was the third mission in the Chandrayaan programme, a series of lunar-exploration missions developed by ISRO...",
                    key_points: ["Soft landing on the South Pole", "Pragyan Rover achievements"],
                    examples: ["Shiv Shakti Point", "National Space Day (August 23)"],
                    completed: false
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  },
  {
    id: "p2",
    exam_id: "Group_II",
    title: "Paper II: History, Polity & Society",
    subjects: [
      {
        id: "sub-pol-1",
        title: "Indian Polity & Constitution",
        topics: [
          {
            id: "top-pol-1",
            title: "Fundamental Rights",
            weightage: "High",
            subtopics: [
              {
                id: "subt-pol-1",
                title: "Introduction and Articles 12-13",
                progress: 100,
                concepts: [
                  {
                    id: "c-pol-1",
                    title: "Definition of State (Art 12)",
                    content: "The term 'State' includes the Government and Parliament of India and the Government and the Legislature of each of the States...",
                    key_points: ["Includes local authorities", "Includes statutory or non-statutory authorities like LIC, ONGC"],
                    examples: ["Municipality is a State", "Private bodies acting as agents of State"],
                    completed: true
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        id: "sub-hist-1",
        title: "Socio-Cultural History of Telangana",
        topics: [
          {
            id: "top-hist-1",
            title: "Satavahana Dynasty",
            weightage: "High",
            subtopics: [
              {
                id: "subt-hist-1",
                title: "Administration & Society",
                progress: 20,
                concepts: [
                  {
                    id: "c-hist-1",
                    title: "Gautamiputra Satakarni",
                    content: "The greatest ruler of the Satavahana dynasty, known for his military conquests and social reforms...",
                    key_points: ["Destroyer of Scythians", "Restorer of Satavahana pride"],
                    examples: ["Nasik Inscription of Gautami Balasri"],
                    completed: false
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  },
  {
    id: "p3",
    exam_id: "Group_II",
    title: "Paper III: Economy and Development",
    subjects: [
      {
        id: "eco-1",
        title: "Indian Economy & Challenges",
        topics: [
          {
            id: "top-eco-1",
            title: "Planning in Indian Economy",
            weightage: "Medium",
            subtopics: [
              {
                id: "subt-eco-1",
                title: "Five Year Plans Breakdown",
                progress: 0,
                concepts: [
                  {
                    id: "c-eco-1",
                    title: "NITI Aayog",
                    content: "The National Institution for Transforming India, also called NITI Aayog, is a public policy think tank of the Government of India...",
                    key_points: ["Established in 2015", "Bottom-up approach", "Cooperative federalism"],
                    examples: ["Replacement of Planning Commission"],
                    completed: false
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  },
  {
    id: "p4",
    exam_id: "Group_II",
    title: "Paper IV: Telangana Movement & State Formation",
    subjects: [
      {
        id: "mov-1",
        title: "The Idea of Telangana (1948-1970)",
        topics: [
          {
            id: "top-mov-1",
            title: "Historical Background",
            weightage: "High",
            subtopics: [
              {
                id: "subt-mov-1",
                title: "Mulki Rules & Gentlemen's Agreement",
                progress: 0,
                concepts: [
                  {
                    id: "c-mov-1",
                    title: "Gentlemen's Agreement 1956",
                    content: "Signed between the leaders of Andhra and Telangana before the formation of Andhra Pradesh state...",
                    key_points: ["14 points agreement", "Safeguards for Telangana"],
                    examples: ["Cabinet representation ratios"],
                    completed: false
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  }
];
