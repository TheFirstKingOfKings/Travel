package com.example.hackapp.presentation.base.architecture

import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentTransaction
import com.example.hackapp.R
import com.example.hackapp.util.hideKeyboard
import org.koin.android.ext.android.get
import org.koin.core.qualifier.named
import ru.terrakok.cicerone.Navigator
import ru.terrakok.cicerone.NavigatorHolder
import ru.terrakok.cicerone.android.support.SupportAppNavigator
import ru.terrakok.cicerone.android.support.SupportAppScreen
import ru.terrakok.cicerone.commands.BackTo
import ru.terrakok.cicerone.commands.Command
import ru.terrakok.cicerone.commands.Forward
import ru.terrakok.cicerone.commands.Replace

abstract class FlowFragment : BaseFragment() {

    private val flowCiceroneQualifier
        get() = named(fragmentScopeName + "CICERONE")

    private val flowNavigatorHolderQualifier
        get() = named(fragmentScopeName + "NAVIGATOR")

    protected val flowRouterQualifier
        get() = named(fragmentScopeName)

    override fun onResume() {
        super.onResume()
        get<NavigatorHolder>(flowNavigatorHolderQualifier).setNavigator(navigator)
    }

    protected val navigator: Navigator by lazy {
        object : SupportAppNavigator(this.activity, childFragmentManager, R.id.container) {
            override fun activityBack() {
                onExit()
            }

            override fun setupFragmentTransaction(
                    command: Command?,
                    currentFragment: Fragment?,
                    nextFragment: Fragment?,
                    fragmentTransaction: FragmentTransaction
            ) {
                //fix incorrect order lifecycle callback of MainFlowFragment
                fragmentTransaction.setReorderingAllowed(true)
                view?.hideKeyboard()
            }
        }
    }

    open fun onExit(): Boolean {
        get<FlowRouter>(flowRouterQualifier).finishFlow()
        return false
    }

    override fun onPause() {
        get<NavigatorHolder>(flowNavigatorHolderQualifier).removeNavigator()
        super.onPause()
    }



}

fun Navigator.setLaunchScreen(vararg screens: SupportAppScreen) {
    applyCommands(
            arrayOf(
                    BackTo(null),
                    Replace(screens.first())
            ).plus(
                    screens.drop(1).map { Forward(it) }
            )
    )
}