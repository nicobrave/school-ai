import { useState, useEffect } from 'react'

export default function PlanificadorPage() {
  const [plan, setPlan] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/planificador')
      .then(res => res.json())
      .then(data => {
        setPlan(data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  if (loading) return <p>Cargando planificador…</p>
  return (
    <div>
      <h1 className="text-2xl font-semibold mb-4">Planificador de Clases</h1>
      {plan.length === 0
        ? <p className="text-text-secondary">No hay sesiones creadas.</p>
        : (
          <ul className="space-y-3">
            {plan.map(sesion => (
              <li key={sesion.id} className="card">
                <strong>{sesion.fecha}</strong>: {sesion.tema}
              </li>
            ))}
          </ul>
        )
      }
    </div>
  )
}
