import React from 'react'

const SeatGrid = ({seatPlans}) => {
    const getSeatColorClass = (seatType) => {
        switch(seatType) {
          case 'Premium': return 'bg-red-500';
          case 'VIP': return 'bg-blue-500';
          case 'Standard': return 'bg-green-500';
          case 'Fixed Back': return 'bg-yellow-500';
          case 'Premium Glider': return 'bg-purple-500';
          case 'Individual Chairs': return 'bg-orange-500';
          default: return 'bg-gray-500';
        }
      };
  return (
    <div>
      {seatPlans.map((seatPlan,i)=>
    <div className={`grid grid-cols-${seatPlan.cols} gap-1`}>
        {Array(seatPlan.rows*seatPlan.cols).fill(0).map((_,i)=>
        <div key={i} className={`w-5 h-5 border ${getSeatColorClass(seatPlan.seat_type)}`}
       >

        </div>
        )}

    </div>
    )}
    </div>
  )
}

export default SeatGrid
