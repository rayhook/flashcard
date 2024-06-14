function App() {
  return (
    <div className="bg-slate-700 min-h-screen flex justify-center">
      <div className="bg-gray-500 w-full max-w-screen-xl py-6 px-4">
        <div className="bg-emerald-400 p-4">
          <div className="py-2 px-1 bg-blue-400">
            <h1 className="text-white text-center text-3xl">FlashCard</h1>
          </div>
          <div className="bg-gray-300 py-4 px-2 flex justify-center">
            <div className="w-1/2 bg-purple-300 py-1 px-2">
              <div className="w-full bg-amber-600 py-2">
                <div className="w-1/2 flex justify-between px-1 ">
                  <h3>Name</h3>
                  <h3>Cards</h3>
                </div>
              </div>

              <DeckItem />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

const DeckItem = () => {
  return (
    <div className="py-2 px-1 flex justify-center bg-slate-400">
      <div className="flex justify-between w-full bg-blue-400">
        <div className="px-4 py-1">
          <h1 className=""> Deck1</h1>
        </div>
        <div className="px-4 py-1">
          <h1 className="">33</h1>
        </div>
      </div>
      <div className="flex justify-center w-full bg-blue-200">
        <div className="px-4 py-1">
          <button className="bg-green-300 rounded px-2 py-1"> Rename</button>
        </div>
        <div className="px-4 py-1">
          <button className="bg-red-300 rounded px-2 py-1"> Delete</button>
        </div>
      </div>
    </div>
  );
};
