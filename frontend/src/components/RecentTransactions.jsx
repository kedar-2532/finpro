function RecentTransactions({ transactions }) {
  return (
    <div className="bg-white p-5 rounede-xl shadow">

      <h2 className="test-xl font-bold mb-4">
        Recent Transactions
      </h2>

    {transactions.map((item)=>(

        <div key={item.id} className="flex justift-between border-b py-2">

            <span>
                {item.type}
            </span>

            <span>
                ₹ {item.amount}
            </span>

        </div>

    ))}
    
    </div>
  )
}

export default RecentTransactions
