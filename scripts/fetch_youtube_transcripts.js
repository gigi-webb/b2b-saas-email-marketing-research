// fetch_youtube_transcripts.js
// Fetches YouTube transcripts for B2B SaaS email marketing experts
// Usage: node scripts/fetch_youtube_transcripts.js

const { YoutubeTranscript } = require('youtube-transcript');
const fs = require('fs');
const path = require('path');

const experts = [
  {
    name: 'dave-gerhardt',
    videos: [
      { id: 'mnJL8lWJS5Y', title: 'how-to-crush-email-marketing-b2b-2026' }
    ]
  },
  {
    name: 'brennan-dunn',
    videos: [
      { id: 'MdS-FGdhJMw', title: 'email-marketing-workshop-convertkit' },
      { id: '7QM7F_L0aEU', title: 'email-marketing-framework-changed-my-business' },
      { id: 'fyTfiMOgLbY', title: 'mastering-email-marketing-brennan-dunn' }
    ]
  },
  {
    name: 'val-geisler',
    videos: [
      { id: 'q7-8vKHyq0c', title: 'better-email-marketing-customer-retention' },
      { id: 'ALT-pcEF3WE', title: 'retention-email-tactics-and-strategies' }
    ]
  },
  {
    name: 'kath-pay',
    videos: [
      { id: 'MjyL3JV0FE0', title: 'holistic-email-marketing-strategy-ai-growth' },
      { id: '9y3Gqnmfrr8', title: 'email-marketing-benchmarks-industry-stats' },
      { id: 'CL1HMA71v5I', title: 'mastering-email-marketing-gen-ai-kath-pay' }
    ]
  },
  {
    name: 'katelyn-bourgoin',
    videos: [
      { id: '5ak5IsJ1uCc', title: 'coaching-1m-creator-paid-newsletter-growth' },
      { id: '5rKOB_-yTbk', title: 'newsletter-sponsorship-strategies-1m' },
      { id: 'XUCiFyjtdVI', title: 'studying-fastest-growing-newsletters-1637-hours' }
    ]
  },
  {
    name: 'peep-laja',
    videos: [
      { id: 'q0M6s7LUxqg', title: 'how-to-write-b2b-email-that-converts' }
    ]
  },
  {
    name: 'emily-kramer',
    videos: [
      { id: 'pGPw9ODK_YQ', title: 'paid-marketing-ai-era' },
      { id: '_nxOiJVD-P0', title: 'how-to-grow-newsletter-mkt1-emily-kramer' }
    ]
  },
  {
    name: 'gaetano-dinardi',
    videos: [
      { id: 'jK2M_X5DQXA', title: 'top-saas-growth-strategies-that-work' },
      { id: 'L3WdJM4kpZE', title: 'how-to-grow-email-list-easy-free' },
      { id: 'aDHlTtKhqqI', title: 'how-to-scale-0-to-200k-visits' }
    ]
  }
];

async function fetchTranscript(expert, video) {
  try {
    console.log(`Fetching: ${expert.name} / ${video.title}...`);

    const transcript = await YoutubeTranscript.fetchTranscript(video.id);
    const text = transcript.map(t => t.text).join(' ');

    const outputDir = path.join(
      __dirname,
      '../research/youtube-transcripts',
      expert.name
    );

    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }

    const outputPath = path.join(outputDir, `${video.title}.md`);

    const content = `# ${video.title}

**Expert:** ${expert.name}
**Video ID:** ${video.id}
**URL:** https://youtube.com/watch?v=${video.id}
**Fetched:** ${new Date().toISOString()}

---

## Raw Transcript

${text}

---

## Key Insights

- [To be extracted after review]
- [To be extracted after review]
- [To be extracted after review]
`;

    fs.writeFileSync(outputPath, content);
    console.log(`✅ Saved: ${expert.name}/${video.title}.md`);

  } catch (error) {
    if (error.message && error.message.includes('disabled')) {
      console.log(`⚠️  SKIP ${expert.name}/${video.title}: Subtitles disabled`);
    } else if (error.message && error.message.includes('Could not find')) {
      console.log(`⚠️  SKIP ${expert.name}/${video.title}: Video not found`);
    } else {
      console.log(`❌ ERROR ${expert.name}/${video.title}: ${error.message}`);
    }
  }
}

async function main() {
  const totalVideos = experts.reduce((sum, e) => sum + e.videos.length, 0);
  console.log(`Starting YouTube transcript fetch...`);
  console.log(`Experts: ${experts.length} | Videos: ${totalVideos}\n`);

  for (const expert of experts) {
    for (const video of expert.videos) {
      await fetchTranscript(expert, video);
      await new Promise(resolve => setTimeout(resolve, 1500));
    }
  }

  console.log('\nDone. Check /research/youtube-transcripts/ for output.');
}

main();