# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 6:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 664 windows, 18355 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 343 | 34.1 | 35.4 | $-267.49 | -7.8% | $732.51 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1558 | 50.6 | 49.6 | $-388.96 | -2.5% | $611.04 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1884 | 51.5 | 50.9 | $-567.78 | -3.0% | $432.22 | -1.3 | done | can't tell from luck |
| trend_filter | 1065 | 50.4 | 51.0 | $-575.94 | -5.4% | $424.06 | -1.8 | done | can't tell from luck |
| value_ev10 | 844 | 38.2 | 39.5 | $-631.06 | -7.5% | $368.94 | -1.8 | done | can't tell from luck |
| value_ev5 | 1275 | 40.6 | 41.4 | $-736.42 | -5.8% | $263.58 | -1.8 | done | can't tell from luck |
| coinflip | 2648 | 50.2 | 50.4 | $-1141.36 | -4.3% | $-141.36 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1558 | 49.4 | 51.3 | $-1257.16 | -8.1% | $-257.16 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 1884 | 48.5 | 50.1 | $-1296.96 | -6.9% | $-296.96 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2648 | 50.8 | 51.8 | $-1449.33 | -5.5% | $-449.33 | -2.9 | done | losing for real |
| always_up | 2648 | 47.7 | 49.7 | $-2161.85 | -8.2% | $-1161.85 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4174 | 48.3 | 49.3 | $-2576.62 |
| ETH | 4577 | 48.2 | 48.7 | $-2835.77 |
| SOL | 4779 | 48.2 | 48.8 | $-2788.68 |
| XRP | 4825 | 48.6 | 48.6 | $-2273.24 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
