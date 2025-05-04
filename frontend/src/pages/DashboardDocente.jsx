import { Link } from 'react-router-dom'

export default function DashboardDocente() {
  return (
    <div className="grid gap-6">
      <h1 className="text-2xl font-bold mb-4">Bienvenido/a a School AI</h1>
      <p className="text-text-secondary mb-6">
        Selecciona una funcionalidad para comenzar:
      </p>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card titulo="Evaluaciones Diferenciadas" to="/evaluaciones" color="bg-primary" />
        <Card titulo="Generador de Actividades" to="/actividades" color="bg-secondary" />
        <Card titulo="Planificador de Clases" to="/planificador" color="bg-accent" />
        <Card titulo="Tabulación de Pruebas" to="/tabulador" color="bg-primary" />
      </div>
    </div>
  )
}

function Card({ titulo, to, color }) {
  return (
    <Link to={to} className={`block p-6 rounded-xl text-white shadow-card ${color} hover:opacity-90 transition`}>
      <h2 className="text-xl font-semibold">{titulo}</h2>
      <p className="text-sm mt-2">Ir a esta sección →</p>
    </Link>
  )
}
