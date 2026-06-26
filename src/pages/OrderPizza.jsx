import { useState, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import axios from 'axios';
import { addToCart } from '../store/cartSlice';

const OrderPizza = () => {
  const [pizzas, setPizzas] = useState([]);
  const [loading, setLoading] = useState(true);
  const dispatch = useDispatch();

  useEffect(() => {
    axios
      .get('/data/pizzas.json')
      .then((res) => {
        setPizzas(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Error loading pizzas:', err);
        setLoading(false);
      });
  }, []);

  const handleAddToCart = (pizza) => {
    dispatch(addToCart(pizza));
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-amber-500"></div>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {pizzas.map((pizza) => (
          <div
            key={pizza.id}
            className="bg-white border border-gray-200 rounded-lg shadow-sm p-5 flex gap-4 hover:shadow-md transition-shadow duration-200"
          >
            <div className="flex-1 min-w-0">
              <div className="flex items-start gap-2 mb-2">
                <h2 className="text-lg font-bold text-gray-800 leading-tight">{pizza.name}</h2>
                <span
                  className={`w-4 h-4 border-2 flex-shrink-0 mt-1 flex items-center justify-center ${
                    pizza.type === 'veg' ? 'border-green-600' : 'border-red-600'
                  }`}
                >
                  <span
                    className={`w-2 h-2 rounded-full ${
                      pizza.type === 'veg' ? 'bg-green-600' : 'bg-red-600'
                    }`}
                  ></span>
                </span>
              </div>

              <p className="text-gray-500 text-xs mb-3 leading-relaxed">{pizza.description}</p>

              <p className="text-amber-600 font-bold text-lg mb-3">
                ₹{Number(pizza.price).toFixed(2)}
              </p>

              <div className="mb-2">
                <span className="text-xs font-semibold text-gray-700">Ingredients : </span>
                <span className="text-xs text-gray-500">
                  {pizza.ingredients.join(', ')}
                </span>
              </div>

              <div className="mb-3">
                <span className="text-xs font-semibold text-gray-700">Toppings : </span>
                <span className="text-xs text-gray-500">
                  {pizza.topping.join(', ')}
                </span>
              </div>

              <button
                onClick={() => handleAddToCart(pizza)}
                className="bg-amber-500 hover:bg-amber-600 text-white text-xs font-semibold px-4 py-2 rounded transition-colors duration-200 cursor-pointer"
              >
                Add to Cart
              </button>
            </div>

            <div className="w-36 h-36 flex-shrink-0">
              <img
                src={pizza.image}
                alt={pizza.name}
                className="w-full h-full object-cover rounded-lg"
                onError={(e) => {
                  e.target.src = 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=200&h=200&fit=crop';
                }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default OrderPizza;
