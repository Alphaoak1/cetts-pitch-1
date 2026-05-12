export const metadata = {
  title: "BetulaR — Technical Supplement",
  description: "Industrial Cell Architecture: Process flow diagram, equipment specifications, and scaling analysis.",
};

export default function TechSuppLayout({ children }) {
  return (
    <>
      <link
        href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@300;400;600;700&family=Barlow+Condensed:wght@300;400;600;700&display=swap"
        rel="stylesheet"
      />
      {children}
    </>
  );
}
