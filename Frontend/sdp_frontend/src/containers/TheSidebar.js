import React from "react";
import { useSelector, useDispatch } from "react-redux";
import {
  CCreateElement,
  CSidebar,
  CSidebarBrand,
  CSidebarNav,
  CSidebarNavDivider,
  CSidebarNavTitle,
  CSidebarMinimizer,
  CSidebarNavDropdown,
  CSidebarNavItem,
} from "@coreui/react";

import CIcon from "@coreui/icons-react";

// sidebar nav config
import navigation from "./_nav";
import * as userActions from "../store/modules/user/actions";

const TheSidebar = () => {
  const dispatch = useDispatch();
  const show = useSelector((state) => state.user.sidebarShow);

  return (
    <CSidebar
      show={show}
      onShowChange={(val) => dispatch(userActions.set_sidebar(val))}
    >
      <CSidebarBrand className="d-md-down-none" to="/dashboard">
        박원보
      </CSidebarBrand>
      <CSidebarNav>
        <CCreateElement
          items={navigation}
          components={{
            CSidebarNavDivider,
            CSidebarNavDropdown,
            CSidebarNavItem,
            CSidebarNavTitle,
          }}
        />
      </CSidebarNav>
      <CSidebarMinimizer className="c-d-md-down-none" />
    </CSidebar>
  );
};

export default React.memo(TheSidebar);
