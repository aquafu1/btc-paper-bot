# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 4:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 513 windows, 14147 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 265 | 34.3 | 35.5 | $-188.91 | -7.1% | $811.09 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1202 | 51.1 | 49.8 | $-210.20 | -1.7% | $789.80 | -0.6 | done | can't tell from luck |
| value_ev10 | 662 | 38.1 | 39.7 | $-503.23 | -7.6% | $496.77 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1435 | 49.6 | 49.6 | $-594.62 | -4.1% | $405.38 | -1.6 | done | can't tell from luck |
| trend_filter | 830 | 49.3 | 50.8 | $-599.18 | -7.2% | $400.82 | -2.1 | done | losing for real |
| value_ev5 | 984 | 39.9 | 41.5 | $-719.96 | -7.3% | $280.04 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1435 | 50.4 | 51.6 | $-930.10 | -6.5% | $69.90 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1202 | 48.9 | 51.3 | $-1085.34 | -9.0% | $-85.34 | -3.2 | done | losing for real |
| coinflip | 2044 | 50.0 | 50.7 | $-1088.21 | -5.3% | $-88.21 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 2044 | 49.4 | 51.6 | $-1647.95 | -8.1% | $-647.95 | -3.8 | done | losing for real |
| always_up | 2044 | 46.2 | 50.0 | $-2391.50 | -11.7% | $-1391.50 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3200 | 47.2 | 49.2 | $-2621.95 |
| ETH | 3534 | 47.9 | 48.7 | $-2357.59 |
| SOL | 3687 | 47.6 | 49.0 | $-2763.76 |
| XRP | 3726 | 48.3 | 48.8 | $-2215.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
