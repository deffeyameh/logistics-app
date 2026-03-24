import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_KEY
)

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*')

  const { code } = req.query

  if (!code) return res.status(400).json({ error: 'กรุณาใส่ tracking code' })

  // หาจาก sm_code
  const { data: byCode } = await supabase
    .from('containers')
    .select('*, products(*)')
    .ilike('sm_code', `%${code}%`)
    .limit(5)

  // หาจาก product tracking
  const { data: byTracking } = await supabase
    .from('products')
    .select('*, containers(*)')
    .ilike('product_tracking', `%${code}%`)
    .limit(5)

  res.json({
    by_sm_code: byCode || [],
    by_tracking: byTracking || []
  })
}
