import { Container } from "./Container";
import { Breadcrumb, type Crumb } from "./Breadcrumb";

type PageIntroProps = {
  title: string;
  description: string;
  crumbs?: Crumb[];
};

export function PageIntro({ title, description, crumbs }: PageIntroProps) {
  return (
    <section className="border-b border-ink/10 bg-mist py-14 sm:py-16">
      <Container>
        {crumbs ? <Breadcrumb items={crumbs} /> : null}
        <h1 className="font-display text-4xl font-semibold tracking-tight text-ink sm:text-5xl">
          {title}
        </h1>
        <p className="mt-4 max-w-2xl text-base leading-relaxed text-slate sm:text-lg">
          {description}
        </p>
      </Container>
    </section>
  );
}
