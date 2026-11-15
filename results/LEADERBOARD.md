# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 5:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 420 windows, 11569 settled trades, 31 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 209 | 34.9 | 36.4 | $-156.95 | -7.5% | $843.05 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 991 | 50.8 | 50.1 | $-274.34 | -2.8% | $725.66 | -0.9 | done | can't tell from luck |
| value_ev10 | 537 | 39.7 | 40.4 | $-291.49 | -5.4% | $708.51 | -1.1 | done | can't tell from luck |
| value_ev5 | 809 | 41.7 | 42.1 | $-398.73 | -4.9% | $601.27 | -1.2 | done | can't tell from luck |
| trend_filter | 662 | 49.5 | 50.8 | $-422.59 | -6.4% | $577.41 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1171 | 49.2 | 50.0 | $-606.62 | -5.2% | $393.38 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1171 | 50.8 | 51.8 | $-700.04 | -6.0% | $299.96 | -2.1 | done | losing for real |
| coinflip | 1676 | 50.4 | 50.9 | $-795.49 | -4.7% | $204.51 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 991 | 49.2 | 51.8 | $-888.60 | -9.0% | $111.40 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1676 | 49.5 | 51.6 | $-1270.83 | -7.6% | $-270.83 | -3.2 | done | losing for real |
| always_up | 1676 | 46.0 | 50.7 | $-2131.09 | -12.7% | $-1131.09 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2619 | 47.7 | 49.4 | $-1887.73 |
| ETH | 2907 | 48.0 | 49.0 | $-1825.43 |
| SOL | 2996 | 47.7 | 49.5 | $-2503.83 |
| XRP | 3047 | 48.7 | 49.3 | $-1719.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
