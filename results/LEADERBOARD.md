# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 1:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 407 windows, 11163 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 202 | 36.1 | 36.5 | $-86.95 | -4.3% | $913.05 | -0.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 951 | 51.2 | 49.9 | $-151.49 | -1.6% | $848.51 | -0.5 | done | can't tell from luck |
| value_ev10 | 523 | 40.2 | 40.5 | $-214.41 | -4.1% | $785.59 | -0.8 | done | can't tell from luck |
| trend_filter | 630 | 50.5 | 50.7 | $-273.07 | -4.3% | $726.93 | -1.1 | done | can't tell from luck |
| value_ev5 | 788 | 41.9 | 42.2 | $-334.08 | -4.2% | $665.92 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1123 | 49.6 | 49.9 | $-466.43 | -4.2% | $533.57 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1123 | 50.4 | 51.9 | $-763.05 | -6.8% | $236.95 | -2.4 | done | losing for real |
| coinflip | 1624 | 50.1 | 50.9 | $-824.85 | -5.1% | $175.15 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 951 | 48.8 | 52.0 | $-937.29 | -9.9% | $62.71 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1624 | 50.0 | 51.6 | $-1054.42 | -6.5% | $-54.42 | -2.7 | done | losing for real |
| always_up | 1624 | 45.6 | 50.7 | $-2191.00 | -13.5% | $-1191.00 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2521 | 47.7 | 49.5 | $-1795.10 |
| ETH | 2804 | 47.9 | 48.9 | $-1753.27 |
| SOL | 2887 | 47.9 | 49.5 | $-2216.80 |
| XRP | 2951 | 48.9 | 49.3 | $-1531.86 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
