import React from "react";
import HeaderOne from "../components/headers/header-one";
import Breadcrubs from "../components/common/widgets/breadcrubs";
import Helmet from "react-helmet";
import favicon from "../public/assets/images/favicon/1.png";
import MasterFooter from "../components/footers/common/MasterFooter";

const Layout = ({children,title, parent, subTitle }) => {
  return (
    <>
   <Helmet>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" type="image/x-icon" href={"/assets/images/favicon/1.png"} />
      </Helmet>
    <HeaderOne topClass="top-header" logoName="logo-layeli.jpg" />
    <Breadcrubs title={title} parent={parent} subTitle={subTitle} />
    <>{children}</>
    <MasterFooter
      footerClass={`footer-light `}
      footerLayOut={"light-layout upper-footer"}
      footerSection={"small-section border-section border-top-0"}
      belowSection={"section-b-space light-layout"}
      newLatter={true}
    />
  </>
  )
}

export default Layout
 