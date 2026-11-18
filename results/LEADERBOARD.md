# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 4:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 705 windows, 19475 settled trades, 25 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 373 | 34.0 | 34.9 | $-254.03 | -6.8% | $745.97 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1635 | 50.2 | 49.4 | $-512.57 | -3.1% | $487.43 | -1.3 | done | can't tell from luck |
| value_ev10 | 902 | 38.2 | 39.1 | $-543.27 | -6.0% | $456.73 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1997 | 51.6 | 50.8 | $-550.90 | -2.8% | $449.10 | -1.2 | done | can't tell from luck |
| trend_filter | 1134 | 50.3 | 50.9 | $-625.44 | -5.5% | $374.56 | -1.9 | done | can't tell from luck |
| value_ev5 | 1357 | 40.8 | 41.1 | $-635.25 | -4.7% | $364.75 | -1.5 | done | can't tell from luck |
| coinflip | 2815 | 50.2 | 50.3 | $-1207.20 | -4.3% | $-207.20 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1635 | 49.8 | 51.4 | $-1229.49 | -7.5% | $-229.49 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 1997 | 48.4 | 50.0 | $-1402.30 | -7.0% | $-402.30 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 2815 | 51.0 | 51.8 | $-1441.55 | -5.1% | $-441.55 | -2.8 | done | losing for real |
| always_up | 2815 | 47.4 | 49.6 | $-2400.46 | -8.5% | $-1400.46 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4412 | 48.2 | 49.1 | $-2576.36 |
| ETH | 4843 | 48.3 | 48.5 | $-2774.04 |
| SOL | 5085 | 48.2 | 48.7 | $-2899.80 |
| XRP | 5135 | 48.5 | 48.4 | $-2552.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
