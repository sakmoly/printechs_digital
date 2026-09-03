import { notFound } from "next/navigation";
import { SuccessStoryView } from "@/components/stories/SuccessStoryView";
import { buildMetadata } from "@/lib/seo";
import {
  fetchSuccessStory,
  fetchSuccessStorySlugs,
} from "@/lib/success-story-service";

export const revalidate = 60;

type Props = { params: { slug: string } };

export async function generateStaticParams() {
  const slugs = await fetchSuccessStorySlugs();
  return slugs.map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: Props) {
  const story = await fetchSuccessStory(params.slug);
  if (!story) {
    return buildMetadata({
      title: "Success Story | Printechs",
      description: "Customer installation story from Printechs.",
    });
  }
  return buildMetadata(story.seo);
}

export default async function SuccessStoryPage({ params }: Props) {
  const story = await fetchSuccessStory(params.slug);
  if (!story) notFound();

  return <SuccessStoryView story={story} />;
}
