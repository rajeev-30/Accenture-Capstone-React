import { useState, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import axios from 'axios';
import { addToCart } from '../store/cartSlice';
import { useNavigate } from 'react-router-dom';

const BuildPizza = () => {
  const [ingredients, setIngredients] = useState([]);
  const [selected, setSelected] = useState({});
  const [loading, setLoading] = useState(true);
  const dispatch = useDispatch();
  const navigate = useNavigate();

  useEffect(() => {
    axios
      .get('/data/ingredients.json')
      .then((res) => {
        setIngredients(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Error loading ingredients:', err);
        setLoading(false);
      });
  }, []);

  const handleToggle = (ingredient) => {
    setSelected((prev) => {
      const newSelected = { ...prev };
      if (newSelected[ingredient.id]) {
        delete newSelected[ingredient.id];
      } else {
        newSelected[ingredient.id] = ingredient;
      }
      return newSelected;
    });
  };

  const handleAdd = (ingredient) => {
    if (!selected[ingredient.id]) {
      setSelected((prev) => ({ ...prev, [ingredient.id]: ingredient }));
    }
  };

  const totalCost = Object.values(selected).reduce(
    (sum, ing) => sum + Number(ing.price),
    0
  );

  const handleBuildPizza = () => {
    if (Object.keys(selected).length === 0) {
      alert('Please select at least one ingredient to build your pizza!');
      return;
    }

    const selectedList = Object.values(selected);
    const totalPrice = selectedList.reduce((sum, ing) => sum + Number(ing.price), 0);

    const customPizza = {
      id: `custom-${Date.now()}`,
      name: 'Build Ur Pizza',
      type: 'custom',
      isCustom: true,
      price: totalPrice,
      image: 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=200&h=200&fit=crop',
      description: 'Custom built pizza with selected ingredients',
      selectedIngredients: selectedList,
    };

    dispatch(addToCart(customPizza));
    setSelected({});
    navigate('/cart');
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-amber-500"></div>
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto px-4 py-8">
      <p className="text-gray-600 text-sm mb-6 text-center">
        Pizzeria now gives you options to build your own pizza. Customize your pizza by choosing
        ingredients from the list given below
      </p>

      <div className="bg-white border border-gray-200 rounded-lg shadow-sm overflow-hidden">
        <table className="w-full">
          <tbody>
            {ingredients.map((ingredient) => (
              <tr
                key={ingredient.id}
                className="border-b border-gray-100 hover:bg-gray-50 transition-colors"
              >
                <td className="p-3 w-20">
                  <img
                    src={ingredient.image}
                    alt={ingredient.tname}
                    className="w-16 h-12 object-cover rounded"
                    onError={(e) => {
                      e.target.src = 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=100&h=80&fit=crop';
                    }}
                  />
                </td>

                <td className="p-3">
                  <span className="font-semibold text-gray-800 text-sm">{ingredient.tname}</span>
                  <span className="text-gray-600 text-sm ml-4">
                    ₹{Number(ingredient.price).toFixed(2)}
                  </span>
                </td>

                <td className="p-3 text-center w-12">
                  <input
                    type="checkbox"
                    checked={!!selected[ingredient.id]}
                    onChange={() => handleToggle(ingredient)}
                    className="w-4 h-4 accent-amber-500 cursor-pointer"
                  />
                </td>

                <td className="p-3 w-16">
                  <button
                    onClick={() => handleAdd(ingredient)}
                    className="text-orange-500 hover:text-orange-700 text-sm font-medium cursor-pointer bg-transparent border-none"
                  >
                    Add
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="mt-6 text-center">
        <p className="text-blue-800 font-bold text-lg">
          Total Cost : {totalCost}
        </p>
      </div>

      <div className="mt-4 text-center">
        <button
          onClick={handleBuildPizza}
          className="bg-[#1a1a1a] hover:bg-gray-800 text-amber-400 font-semibold px-8 py-3 rounded border-2 border-amber-500 transition-colors duration-200 cursor-pointer text-sm"
        >
          Build Ur Pizza
        </button>
      </div>
    </div>
  );
};

export default BuildPizza;
