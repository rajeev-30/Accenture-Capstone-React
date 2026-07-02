import { useDispatch } from 'react-redux';
import { useNavigate, useLocation } from 'react-router-dom';
import { clearCart } from '../store/cartSlice';
import { useEffect } from 'react';

const Checkout = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const location = useLocation();
  const total = location.state?.total || 0;

  useEffect(() => {
    dispatch(clearCart());
  }, [dispatch]);

  return (
    <div className="max-w-2xl mx-auto px-4 py-20 text-center">
      <div className="bg-white border border-gray-200 rounded-lg shadow-sm p-10">
        <h2 className="text-2xl font-bold text-gray-800 mb-3">Order Placed Successfully!</h2>
        <p className="text-gray-600 text-lg">
          Your order of <span className="font-bold text-amber-600">₹{total.toFixed(2)}</span> will be delivered within 45 minutes.
        </p>
        <button
          onClick={() => navigate('/')}
          className="mt-8 bg-amber-500 hover:bg-amber-600 text-white font-semibold px-8 py-3 rounded transition-colors cursor-pointer"
        >
          Back to Home
        </button>
      </div>
    </div>
  );
};

export default Checkout;
