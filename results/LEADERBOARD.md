# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 4:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 995 windows, 27679 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 508 | 34.1 | 34.9 | $-315.26 | -6.2% | $684.74 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2824 | 51.1 | 50.4 | $-854.05 | -3.0% | $145.95 | -1.6 | done | can't tell from luck |
| value_ev10 | 1264 | 37.4 | 39.1 | $-928.79 | -7.3% | $71.21 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2379 | 49.8 | 49.7 | $-1116.46 | -4.7% | $-116.46 | -2.3 | done | losing for real |
| trend_filter | 1660 | 49.5 | 50.8 | $-1254.66 | -7.6% | $-254.66 | -3.2 | done | losing for real |
| value_ev5 | 1916 | 39.5 | 41.0 | $-1290.50 | -6.7% | $-290.50 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2379 | 50.2 | 50.9 | $-1535.71 | -6.5% | $-535.71 | -3.2 | done | losing for real |
| coinflip | 3975 | 50.3 | 50.3 | $-1746.78 | -4.4% | $-746.78 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2824 | 48.9 | 50.4 | $-1934.40 | -6.8% | $-934.40 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3975 | 50.7 | 51.5 | $-2213.26 | -5.6% | $-1213.26 | -3.6 | done | losing for real |
| always_up | 3975 | 46.8 | 49.6 | $-3943.57 | -9.9% | $-2943.57 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6312 | 48.2 | 49.1 | $-3557.27 |
| ETH | 6878 | 48.0 | 48.5 | $-4545.43 |
| SOL | 7228 | 48.1 | 48.6 | $-4291.79 |
| XRP | 7261 | 48.0 | 48.4 | $-4738.95 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
