# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 8:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 672 windows, 18618 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 348 | 34.5 | 35.2 | $-217.83 | -6.3% | $782.17 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1584 | 50.8 | 49.6 | $-304.53 | -1.9% | $695.47 | -0.8 | done | can't tell from luck |
| trend_filter | 1085 | 50.7 | 50.9 | $-492.53 | -4.5% | $507.47 | -1.5 | done | can't tell from luck |
| value_ev10 | 858 | 38.5 | 39.4 | $-525.66 | -6.1% | $474.34 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1908 | 51.3 | 50.9 | $-641.33 | -3.4% | $358.67 | -1.5 | done | can't tell from luck |
| value_ev5 | 1291 | 40.7 | 41.3 | $-651.02 | -5.0% | $348.98 | -1.5 | done | can't tell from luck |
| coinflip | 2684 | 50.2 | 50.4 | $-1128.64 | -4.2% | $-128.64 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1908 | 48.7 | 50.0 | $-1210.71 | -6.3% | $-210.71 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1584 | 49.2 | 51.3 | $-1335.54 | -8.4% | $-335.54 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2684 | 50.8 | 51.8 | $-1430.40 | -5.3% | $-430.40 | -2.9 | done | losing for real |
| always_up | 2684 | 47.2 | 49.7 | $-2423.05 | -9.0% | $-1423.05 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4233 | 48.3 | 49.2 | $-2486.12 |
| ETH | 4643 | 48.3 | 48.6 | $-2711.39 |
| SOL | 4847 | 48.2 | 48.7 | $-2807.98 |
| XRP | 4895 | 48.5 | 48.5 | $-2355.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
