import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, Legend} from "recharts";

function MonthlyChart({data}){

    console.log("CHART DATA:",data)

    return(
        <div className="bg-white p-5 rounded-xl shadow mt-6">

            <h2 className="text-xl font-bold mb-4">Monthly Summary</h2>

            <div className="w-full h-[350px]">

            <ResponsiveContainer width="100%" height="100%">

                <LineChart data={data} margin={{top:20, right:20, left:10, botton:10}}>

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis dataKey='month' />

                    <YAxis />

                    <Tooltip />

                    <Legend /> 

                    <Line type='monotone' dataKey='income' />

                    <Line type='monotone' dataKey='expense' />

                </LineChart>
                
            </ResponsiveContainer>

            </div>

        </div>
    )
}
export default MonthlyChart