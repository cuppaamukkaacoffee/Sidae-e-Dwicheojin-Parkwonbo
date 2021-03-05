import React from 'react'
import CIcon from '@coreui/icons-react'

const _nav =  [
  {
    _tag: 'CSidebarNavItem',
    name: 'Dashboard',
    to: '/dashboard',
    icon: <CIcon name="cil-speedometer" customClasses="c-sidebar-nav-icon"/>,
  },
  {
    _tag: 'CSidebarNavTitle',
    _children: ['Scan']
  },
  {
    _tag: 'CSidebarNavDropdown',
    name: 'Scanner',
    route: '/scans',
    icon: 'cil-speedometer',
    _children: [
      {
        _tag: 'CSidebarNavItem',
        name: 'Web scan',
        to: '/scans/webscan',
      },
      {
        _tag: 'CSidebarNavItem',
        name: 'Network scan',
        to: '/scans/netscan',
      },
    ],
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Target',
    icon: 'cil-puzzle',
    to: '/target',
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Vulnerabilities',
    icon: 'cil-bell',
    to: '/vulnerabilities',
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Result',
    icon: 'cil-laptop',
    to: '/result',
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Report',
    icon: 'cil-moon',
    to: '/report',
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'User',
    icon: 'cil-user',
    to: '/user',
  },

]

export default _nav
