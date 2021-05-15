/**
  The Blacklist - s01e17 24:40 
*/




//////////////////////
// --- Top Pane --- //
//////////////////////

productId = (String)session.getAttribute("aTControllerProductId");
primaryTitle = (String)session.getAttribute("aTControllerPrimaryTitle");

// Column to be sorted
if(req.getParameter("sortBy").equals(""))
{
  sortCol = (String)session.getAttribute("aTControllerSortCol");
}
else
{
  sortCol = req.getParameter("sortBy");
}
/**
 * Order in which the column is to be sorted - ascending
 * or descending
 */
if(req.getParameter("sortOrder").equals(""))
{
  sortOrder = (String)session.getAttribute("aTControllerSortOrder");
}
else
{
  sortOrder = req.getParameter("sortOrder");
}
// Criteria for titles - All titles or Only Released titles
if(req.getParameter("releasedOnly") != null)
{
  if(req.getParameter("releasedOnly").equals("Y"))
  {
    filter = Constants.AlternateTitles.ALT_RELEASED_ONLY;
  }
  else 

  
    
    
    
///////////////////////
// --- Left Pane --- //
///////////////////////
(join=true)
public void processMassCreate(){
	AlphaTree tree = (AlphaTree)Component.getAlphaTree().tree.setMassCreateTree();
	this.alpTitle = new Alpha();
	alpha.setMode(alpha.getTree());
	HashMap<BigDecimal.String>());
	alpha.getAlphaTitle().
	this.setChkMandForEdit().setError(true);
	// added for REQ0020672-RITM0014335
	// Create Functionality
	this.errorMessages = null;
	initializeRootNode();
}
	
private void resetMassCreate(){
	this.alpTitle  = new Alpha();
	this.alpTitle.setColor
	this.setProductPickList(LinkedList<SelectItem>
	this.setProductSelected
	this.alpTitle.setAlpha
	setDecimal(Constants.AL

             
             
             

/////////////////////////
// --- Bottom Pane --- //
/////////////////////////
             
protected Forward begin() throws ProductRightsException. java.rmi
{
		String lProductId = this.getRequest().getParameter(this.PARAMETER
    try
    {
      if (null != lProductId)
      {
        this.productTO = getProduct(Long.valueOf(lProductId).longValue());
        //Format primary title
        this.formatTitle();
        this.setAccess();
      }
      this.setGPMS2Tabs(TabUtils.TAB_ID_ALTERNATE_TITLES.lProductId.true);
    }
    catch(ProductRightsException pre)
    {
      pre.printStackTrace();
      throw pre;
    }
    catch(RemoteException re)
    {
      re.printStackTrace();
      throw re;
    }
    return new Forward("success");
}
