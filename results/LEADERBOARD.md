# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 4:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 611 windows, 16875 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1425 | 51.2 | 49.7 | $-194.41 | -1.4% | $805.59 | -0.5 | done | can't tell from luck |
| value_ev20 | 327 | 34.3 | 35.2 | $-244.70 | -7.5% | $755.30 | -1.0 | done | can't tell from luck |
| trend_filter | 972 | 50.3 | 51.0 | $-545.89 | -5.6% | $454.11 | -1.8 | done | can't tell from luck |
| value_ev10 | 785 | 38.2 | 39.4 | $-548.33 | -7.0% | $451.67 | -1.6 | done | can't tell from luck |
| value_ev5 | 1183 | 40.5 | 41.3 | $-691.34 | -5.8% | $308.66 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1725 | 50.6 | 50.9 | $-836.98 | -4.9% | $163.02 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1725 | 49.4 | 50.1 | $-927.85 | -5.4% | $72.15 | -2.2 | done | losing for real |
| coinflip | 2436 | 50.0 | 50.5 | $-1193.20 | -4.9% | $-193.20 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1425 | 48.8 | 51.3 | $-1349.09 | -9.5% | $-349.09 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2436 | 50.3 | 51.8 | $-1579.17 | -6.5% | $-579.17 | -3.3 | done | losing for real |
| always_up | 2436 | 46.9 | 49.8 | $-2372.27 | -9.7% | $-1372.27 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3834 | 48.0 | 49.2 | $-2525.13 |
| ETH | 4218 | 48.0 | 48.6 | $-2721.73 |
| SOL | 4385 | 47.9 | 48.8 | $-2918.43 |
| XRP | 4438 | 48.4 | 48.6 | $-2317.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
