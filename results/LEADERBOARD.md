# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 6:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1193 windows, 32963 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 643 | 34.8 | 35.3 | $-378.79 | -5.9% | $621.21 | -1.1 | done | can't tell from luck |
| value_ev10 | 1570 | 38.6 | 39.2 | $-814.19 | -5.2% | $185.81 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3301 | 50.9 | 50.3 | $-1027.55 | -3.1% | $-27.55 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2767 | 49.6 | 49.4 | $-1238.22 | -4.5% | $-238.22 | -2.3 | done | losing for real |
| value_ev5 | 2375 | 40.3 | 41.1 | $-1302.33 | -5.5% | $-302.33 | -2.3 | done | losing for real |
| trend_filter | 1947 | 48.7 | 50.5 | $-1652.80 | -8.5% | $-652.80 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2767 | 50.4 | 51.1 | $-1686.50 | -6.1% | $-686.50 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3301 | 49.1 | 50.3 | $-2088.31 | -6.3% | $-1088.31 | -3.7 | done | losing for real |
| coinflip | 4764 | 50.1 | 50.2 | $-2098.90 | -4.4% | $-1098.90 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4764 | 50.1 | 51.4 | $-3059.96 | -6.4% | $-2059.96 | -4.6 | done | losing for real |
| always_up | 4764 | 47.9 | 49.3 | $-3477.61 | -7.3% | $-2477.61 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7569 | 48.1 | 48.9 | $-4244.53 |
| ETH | 8176 | 48.0 | 48.4 | $-5066.97 |
| SOL | 8579 | 48.2 | 48.4 | $-4408.92 |
| XRP | 8639 | 48.1 | 48.2 | $-5104.73 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
