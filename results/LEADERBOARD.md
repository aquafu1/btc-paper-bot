# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 8:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 771 windows, 21268 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 403 | 33.0 | 34.9 | $-381.45 | -9.5% | $618.55 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2170 | 51.3 | 50.6 | $-592.29 | -2.7% | $407.71 | -1.3 | done | can't tell from luck |
| value_ev10 | 975 | 37.6 | 39.1 | $-704.62 | -7.2% | $295.38 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1798 | 49.8 | 49.6 | $-770.69 | -4.3% | $229.31 | -1.8 | done | can't tell from luck |
| trend_filter | 1247 | 49.6 | 50.8 | $-855.43 | -6.9% | $144.57 | -2.5 | done | losing for real |
| value_ev5 | 1473 | 40.0 | 41.0 | $-904.74 | -6.1% | $95.26 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 1798 | 50.2 | 51.2 | $-1166.18 | -6.5% | $-166.18 | -2.8 | done | losing for real |
| coinflip | 3078 | 50.3 | 50.3 | $-1235.06 | -4.0% | $-235.06 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2170 | 48.7 | 50.2 | $-1486.13 | -6.8% | $-486.13 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3078 | 50.9 | 51.6 | $-1553.65 | -5.0% | $-553.65 | -2.9 | done | losing for real |
| always_up | 3078 | 47.1 | 49.5 | $-2795.64 | -9.1% | $-1795.64 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4825 | 48.2 | 49.1 | $-2887.24 |
| ETH | 5306 | 47.9 | 48.5 | $-3575.00 |
| SOL | 5539 | 48.0 | 48.5 | $-3265.39 |
| XRP | 5598 | 48.5 | 48.4 | $-2718.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
