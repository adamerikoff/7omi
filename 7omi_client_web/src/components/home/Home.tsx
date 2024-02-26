import './Home.css'

function Home() {
  return (
    <>
    <div className="py-60 px-6 bg-gray-900 text-white HomeHero">
      <div className="container mx-auto max-w-screen-xl">
        <h2 className="text-4xl font-bold mb-2">
          Connect Effortlessly Across Every Device
        </h2>
        <h3 className="text-2xl mb-8">
          Instantly Reach Out, Anytime, Anywhere
        </h3>
        <button className="bg-white text-gray-900 font-bold rounded-full py-4 px-8 shadow-lg uppercase tracking-wider">
          Register...
        </button>
      </div>
    </div>
    <section className="container mx-auto px-4 p-10">
      <h2 className="text-4xl font-bold text-center text-gray-800 mb-8">
        Features
      </h2>
      <div className="flex flex-wrap items-center mb-20">
        <div className="w-full md:w-1/2 mb-6 md:mb-0">
          <h4 className="text-3xl text-gray-800 font-bold mb-3">Fault Tolerant and Reliable</h4>
          <p className="text-gray-600 mb-8">Built on the rock-solid foundation of Erlang, known for its fault tolerance and reliability, our messaging application ensures that your messages are delivered without fail, even in the face of hardware failures or network issues.</p>
        </div>
        <div className="w-full md:w-1/2">
          <img src="/1.svg" alt="1" className="w-full" />
        </div>
      </div>

      <div className="flex flex-wrap items-center mb-20">
        <div className="w-full md:w-1/2 order-2 md:order-1 md:pr-10">
          <h4 className="text-3xl text-gray-800 font-bold mb-3">Cross-Platform Compatibility</h4>
          <p className="text-gray-600 mb-8">Whether you're using a desktop computer, a smartphone, or a tablet, our messaging application runs seamlessly across all platforms. Say goodbye to compatibility issues and enjoy a consistent user experience wherever you go.</p>
        </div>
        <div className="w-full md:w-1/2 order-1 md:order-2 mb-6 md:mb-0">
          <img src="/2.svg" alt="2" className="w-full" />
        </div>
      </div>

      <div className="flex flex-wrap items-center mb-20">
        <div className="w-full md:w-1/2 mb-6 md:mb-0">
          <h4 className="text-3xl text-gray-800 font-bold mb-3">Scalable and High-Performance</h4>
          <p className="text-gray-600 mb-8">Our application is designed to handle millions of concurrent users with ease. Thanks to Erlang's lightweight processes and built-in scalability features, you can trust our messaging application to perform reliably, no matter how large your user base grows.</p>
        </div>
        <div className="w-full md:w-1/2">
          <img src="/3.svg" alt="3" className="w-full" />
        </div>
      </div>
    </section>
    </>
  )
}

export default Home



