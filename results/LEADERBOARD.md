# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 4:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 369 windows, 9981 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 189 | 38.1 | 36.4 | $+15.78 | +0.8% | $1015.78 | +0.1 | Sat 9:45 PM | too few trades (189/200) |
| value_ev10 | 484 | 41.1 | 40.4 | $-76.39 | -1.6% | $923.61 | -0.3 | done | can't tell from luck |
| value_ev5 | 715 | 42.4 | 42.1 | $-206.26 | -2.9% | $793.74 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 825 | 49.5 | 49.7 | $-394.29 | -4.8% | $605.71 | -1.4 | done | can't tell from luck |
| trend_filter | 553 | 48.8 | 50.5 | $-415.29 | -7.5% | $584.71 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 993 | 51.7 | 52.1 | $-477.22 | -4.8% | $522.78 | -1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 825 | 50.5 | 52.1 | $-556.24 | -6.7% | $443.76 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 993 | 48.3 | 49.6 | $-605.24 | -6.1% | $394.76 | -1.9 | done | can't tell from luck |
| coinflip | 1468 | 49.8 | 50.8 | $-817.89 | -5.6% | $182.11 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1468 | 49.6 | 51.6 | $-1058.99 | -7.2% | $-58.99 | -2.9 | done | losing for real |
| always_up | 1468 | 45.7 | 50.8 | $-1966.53 | -13.4% | $-966.53 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2243 | 47.3 | 49.3 | $-1776.00 |
| ETH | 2511 | 47.7 | 48.9 | $-1737.32 |
| SOL | 2586 | 48.0 | 49.5 | $-1808.98 |
| XRP | 2641 | 48.8 | 49.1 | $-1236.27 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
