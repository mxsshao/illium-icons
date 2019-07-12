package com.mxshao.illium.icons.applications;

import android.support.annotation.NonNull;

import com.dm.material.dashboard.candybar.applications.CandyBarApplication;

public class CandyBar extends CandyBarApplication {
    
    @NonNull
    @Override
    public Configuration onInit() {
        Configuration configuration = new Configuration();

        configuration.setDashboardThemingEnabled(false);
        configuration.setGenerateAppFilter(true);

        return configuration;
    }
}
