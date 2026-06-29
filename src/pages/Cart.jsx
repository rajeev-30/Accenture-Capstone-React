import { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {
  selectCartItems,
  selectPizzaSubtotal,
  selectIngredientsSubtotal,
  selectAggregatedIngredients,
  selectCartTotal,
  incrementQuantity,
  decrementQuantity,
  removeFromCart,
  clearCart,
} from '../store/cartSlice';
import { ArrowBigDown, ArrowDown, Trash2 } from 'lucide-react';

const Cart = () => {
  const items = useSelector(selectCartItems);
  const pizzaSubtotal = useSelector(selectPizzaSubtotal);
  const ingredientsSubtotal = useSelector(selectIngredientsSubtotal);
  const aggregatedIngredients = useSelector(selectAggregatedIngredients);
  const total = useSelector(selectCartTotal);
  const dispatch = useDispatch();
  const [showIngredients, setShowIngredients] = useState(false);

  const handlePay = () => {
    if (items.length === 0) {
      alert('Your cart is empty! Please add items before proceeding.');
      return;
    }
    alert(`Payment successful! Total amount: ₹${total.toFixed(2)}`);
    dispatch(clearCart());
  };

  const handleClear = () => {
    dispatch(clearCart());
  };

  const allItemsSubtotal = items.reduce(
    (total, item) => total + Number(item.price) * item.quantity,
    0
  );

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <div className="flex flex-col lg:flex-row gap-6">
        <div className="flex-1 bg-white border border-gray-200 rounded-lg shadow-sm p-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-6">My Cart</h2>

          {items.length === 0 ? (
            <p className="text-gray-500 text-center py-8">Your cart is empty.</p>
          ) : (
            <>
              {items.map((item) => (
                <div
                  key={item.id}
                  className="flex items-center gap-4 py-4 border-b border-gray-100 last:border-b-0"
                >
                  <img
                    src={item.image}
                    alt={item.name}
                    className="w-14 h-14 object-cover rounded-full flex-shrink-0"
                    onError={(e) => {
                      e.target.src = 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=100&h=100&fit=crop';
                    }}
                  />

                  {item.type !== 'custom' && (
                    <span
                      className={`w-5 h-5 border-2 flex-shrink-0 flex items-center justify-center ${
                        item.type === 'veg' ? 'border-green-600' : 'border-red-600'
                      }`}
                    >
                      <span
                        className={`w-2.5 h-2.5 rounded-full ${
                          item.type === 'veg' ? 'bg-green-600' : 'bg-red-600'
                        }`}
                      ></span>
                    </span>
                  )}
                  {item.type === 'custom' && (
                    <span className="w-5 h-5 border-2 border-amber-500 flex-shrink-0 flex items-center justify-center">
                      <span className="w-2.5 h-2.5 rounded-full bg-amber-500"></span>
                    </span>
                  )}

                  <div className="flex-1 min-w-0">
                    <p className="font-semibold text-gray-800 text-sm">{item.name}</p>
                    {item.isCustom && item.selectedIngredients && (
                      <p className="text-gray-400 text-xs mt-0.5 leading-tight">
                        {item.selectedIngredients.map((ing) => ing.tname).join(', ')}
                      </p>
                    )}
                    <p className="text-gray-500 text-xs">₹{Number(item.price)}</p>
                  </div>

                  <div className="flex items-center gap-0">
                    <button
                      onClick={() =>
                        item.quantity === 1
                          ? dispatch(removeFromCart(item.id))
                          : dispatch(decrementQuantity(item.id))
                      }
                      className="bg-gray-200 hover:bg-gray-300 text-gray-700 font-bold w-8 h-8 rounded-l flex items-center justify-center cursor-pointer border-none text-lg"
                    >
                      -
                    </button>
                    <span className="bg-white border-y border-gray-200 w-10 h-8 flex items-center justify-center text-sm font-semibold">
                      {item.quantity}
                    </span>
                    <button
                      onClick={() => dispatch(incrementQuantity(item.id))}
                      className="bg-gray-500 hover:bg-gray-600 text-white font-bold w-8 h-8 rounded-r flex items-center justify-center cursor-pointer border-none text-lg"
                    >
                      +
                    </button>
                  </div>

                  <p className="font-bold text-gray-800 text-sm w-24 text-right">
                    ₹{(Number(item.price) * item.quantity).toFixed(2)}
                  </p>

                  <button
                    onClick={() => dispatch(removeFromCart(item.id))}
                    className="text-red-500 hover:text-red-700 cursor-pointer bg-transparent border-none text-xl"
                    title="Remove from cart"
                  >
                    <Trash2 className="w-5 h-5" />
                  </button>
                </div>
              ))}

              {items.length > 0 && (
                <div className="text-right mt-4 pt-4 border-t border-gray-200">
                  <p className="text-gray-700 font-semibold">
                    Sub Total : ₹{allItemsSubtotal.toFixed(2)}
                  </p>
                </div>
              )}
            </>
          )}
        </div>

        <div className="w-full lg:w-80 bg-gray-100 border border-gray-200 rounded-lg shadow-sm p-6">
          <h3 className="text-lg font-bold text-gray-800 mb-6">The total amount of</h3>

          <div className="space-y-4">
            <div className="flex justify-between">
              <span className="text-gray-700 text-sm">Pizza</span>
              <span className="text-gray-800 font-semibold text-sm">₹{pizzaSubtotal.toFixed(2)}</span>
            </div>

            <div>
              <div
                className="flex justify-between cursor-pointer"
                onClick={() => setShowIngredients(!showIngredients)}
              >
                <span className="text-gray-700 text-sm flex items-center gap-1">
                  Ingredients
                  <span
                    className={`text-xs transition-transform duration-200 ${
                      showIngredients ? 'rotate-180' : ''
                    }`}
                  >
                    <ArrowDown className='w-4 h-4'/>
                  </span>
                </span>
                <span className="text-gray-800 font-semibold text-sm">
                  ₹{ingredientsSubtotal.toFixed(2)}
                </span>
              </div>

              {showIngredients && aggregatedIngredients.length > 0 && (
                <div className="mt-2 pl-4 space-y-1">
                  {aggregatedIngredients.map((ing) => (
                    <div key={ing.id} className="flex justify-between text-xs text-gray-500">
                      <span>
                        {ing.tname}
                        {ing.count > 1 && (
                          <span className=" ml-1">
                            (x{ing.count})
                          </span>
                        )}
                      </span>
                      <span>₹{(Number(ing.price) * ing.count).toFixed(2)}</span>
                    </div>
                  ))}
                </div>
              )}
            </div>

            <div className="border-t border-gray-300 pt-4 flex justify-between">
              <span className="text-gray-800 font-bold">Total :</span>
              <span className="text-gray-800 font-bold">₹{total.toFixed(2)}</span>
            </div>
          </div>

          <div className="flex gap-4 mt-8">
            <button
              onClick={handlePay}
              className="flex-1 bg-amber-500 hover:bg-amber-600 text-white font-semibold py-2.5 rounded border-2 border-amber-600 transition-colors duration-200 cursor-pointer text-sm"
            >
              Pay
            </button>
            <button
              onClick={handleClear}
              className="flex-1 bg-gray-800 hover:bg-gray-900 text-white font-semibold py-2.5 rounded border-2 border-gray-800 transition-colors duration-200 cursor-pointer text-sm"
            >
              Clear
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Cart;
