import { useState, useEffect } from 'react'

export default function TabuladorPage() {
  const [resultados, setResultados] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/tabulador')
      .then(res => res.json())
      .then(data => {
        setResultados(data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  if (loading) return <p>Cargando tabulación…</p>
  return (
    <div>
      <h1 className="text-2xl font-semibold mb-4">Tabulación de Pruebas</h1>
      {resultados.length === 0
        ? <p className="text-text-secondary">No hay datos tabulados.</p>
        : (
          <table className="min-w-full bg-surface rounded-xl shadow-card">
            <thead>
              <tr>
                <th className="p-3 text-left">Estudiante</th>
                <th className="p-3 text-left">Puntaje</th>
                <th className="p-3 text-left">Comentarios</th>
              </tr>
            </thead>
            <tbody>
              {resultados.map(r => (
                <tr key={r.id} className="border-t">
                  <td className="p-3">{r.nombre}</td>
                  <td className="p-3">{r.puntaje}</td>
                  <td className="p-3">{r.comentario}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )
      }
    </div>
  )
}
