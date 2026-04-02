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
  overallProgress: 0,
  tasks: [
    {
      id: "tsk-1",
      type: "study",
      title: "Fundamental Rights (Polity)",
      description: "Review articles 12 to 35. Focus on exceptions.",
      durationMinutes: 45,
      completed: false,
    },
    {
      id: "tsk-2",
      type: "practice",
      title: "Geography River Systems Quiz",
      description: "Take a 20 question quiz to solidify your strong area.",
      durationMinutes: 20,
      completed: false,
    },
    {
      id: "tsk-3",
      type: "revision",
      title: "Telangana Economy",
      description: "Revisit key dates and figures from the last mock test.",
      durationMinutes: 30,
      completed: true,
    },
  ],
};

export const MOCK_SYLLABUS: Paper[] = [
  {
    id: "p1",
    title: "Paper II: History, Polity & Society",
    subjects: [
      {
        id: "sub-1",
        title: "Indian Polity",
        topics: [
          {
            id: "top-1",
            title: "Fundamental Rights",
            weightage: "High",
            subtopics: [
              {
                id: "subt-1",
                title: "Introduction and Articles 12-13",
                progress: 100,
                concepts: [
                  {
                    id: "c-1",
                    title: "Definition of State (Art 12)",
                    content: "The term 'State' includes the Government and Parliament of India...",
                    keyPoints: ["Includes executive and legislative organs", "Includes local authorities"],
                    examples: ["LIC, ONGC are considered state"],
                    completed: true
                  }
                ]
              },
              {
                id: "subt-2",
                title: "Right to Equality (14-18)",
                progress: 40,
                concepts: [
                  {
                    id: "c-2",
                    title: "Equality before Law (Art 14)",
                    content: "The State shall not deny to any person equality before the law...",
                    keyPoints: ["Rule of law", "Equal protection of laws"],
                    examples: [],
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
