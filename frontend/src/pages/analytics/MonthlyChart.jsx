import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, Legend} from "recharts";

function MonthlyChart({data}){
    return(
        <div className="bg-white p-5 rounded-xl shadow">

            <h2 className="text-xl font-bold mb-4">Monthly Summary</h2>

            <ResponsiveContainer width="100%" height={300}>

                <LineChart data={data}>

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis dataKey='month'/>

                    <YAxis />

                    <Tooltip />

                    <Legend /> 

                    <Line type='monotone' dataKey='expense' />

                </LineChart>
                
            </ResponsiveContainer>

        </div>
    )
}
export default MonthlyChart