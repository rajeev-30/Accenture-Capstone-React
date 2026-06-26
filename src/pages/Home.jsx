const Home = () => {
  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <section className="mb-12">
        <h1 className="text-3xl font-bold text-center mb-6 text-gray-800">Our story</h1>
        <div className="text-gray-600 text-sm leading-relaxed space-y-4">
          <p>
            We believe in good. We launched Fresh Pan Pizza Best Excuse Awards on our Facebook fan page.
            Fans were given situations where they had to come up with wacky and fun excuses. The person
            with the best excuse won the Best Excuse Badge and won Pizzeria&apos;s vouchers. Their enthusiastic
            response proved that Pizzeria&apos;s Fresh Pan Pizza is the Tastiest Pan Pizza. Ever!
          </p>
          <p>
            Ever since we launched the Tastiest Pan Pizza, ever, people have not been able to resist the
            softest, cheesiest, crunchiest, butteriest Domino&apos;s Fresh Pan Pizza. They have been leaving
            the stage in the middle of a performance and even finding excuses to be disqualified in a
            football match.
          </p>
          <p>
            We launched Fresh Pan Pizza Best Excuse Awards on our Facebook fan page. Fans were given
            situations where they had to come up with wacky and fun excuses. The person with the best
            excuse won the Best Excuse Badge and won Domino&apos;s vouchers. Their enthusiastic response proved
            that Pizzeria&apos;s Fresh Pan Pizza is the Tastiest Pan Pizza. Ever!
          </p>
        </div>
      </section>

      <section className="mb-12 flex flex-col md:flex-row items-center gap-8">
        <div className="md:w-1/2">
          <img
            src="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=500&h=350&fit=crop"
            alt="Fresh pizza ingredients"
            className="w-full h-64 object-cover rounded-lg shadow-md"
          />
        </div>
        <div className="md:w-1/2">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">Ingredients</h2>
          <p className="text-gray-600 text-sm leading-relaxed">
            We&apos;re ruthless about goodness. We have no qualms about tearing up a day-old lettuce leaf
            (straight from the farm), or steaming a baby (carrot). Cut. Cut. Chop. Chop. Steam.
            Steam. Stir. Stir. While they&apos;re still young and fresh - that&apos;s our motto. It makes the
            kitchen a better place.
          </p>
        </div>
      </section>

      <section className="mb-12 flex flex-col md:flex-row-reverse items-center gap-8">
        <div className="md:w-1/2">
          <img
            src="https://images.unsplash.com/photo-1556910103-1c02745aae4d?w=500&h=350&fit=crop"
            alt="Our talented chef"
            className="w-full h-64 object-cover rounded-lg shadow-md"
          />
        </div>
        <div className="md:w-1/2">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">Our Chefs</h2>
          <p className="text-gray-600 text-sm leading-relaxed">
            They make sauces sing and salads dance. They create magic with skill, knowledge, passion,
            and stirring spoons (among other things). They make goodness so good, it doesn&apos;t know what
            to do with itself. We do though. We send it to you.
          </p>
        </div>
      </section>

      <section className="mb-12 flex flex-col md:flex-row items-center gap-8">
        <div className="md:w-1/2">
          <img
            src="https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500&h=350&fit=crop"
            alt="Fast delivery timer"
            className="w-full h-64 object-cover rounded-lg shadow-md"
          />
        </div>
        <div className="md:w-1/2">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">45 min delivery</h2>
          <p className="text-gray-600 text-sm leading-relaxed">
            We guarantee delivery within 45 minutes or your pizza is on us! Our efficient delivery
            system ensures your hot, fresh pizza reaches your doorstep in record time.
          </p>
        </div>
      </section>
    </div>
  );
};

export default Home;
