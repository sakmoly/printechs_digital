import { PageIntro } from "./PageIntro";
import { Section } from "./Section";
import { Button } from "./Button";

type StubPageProps = {
  title: string;
  description: string;
  crumbs?: { label: string; href?: string }[];
};

/** Lightweight routing foundation page until detail designs are approved. */
export function StubPage({ title, description, crumbs }: StubPageProps) {
  return (
    <>
      <PageIntro title={title} description={description} crumbs={crumbs} />
      <Section>
        <p className="max-w-2xl text-base leading-relaxed text-slate">
          This route is part of the information architecture foundation. Full page
          design will follow homepage design approval.
        </p>
        <div className="mt-8">
          <Button href="/" variant="ghost">
            Back to homepage prototype
          </Button>
        </div>
      </Section>
    </>
  );
}
