# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 1:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 548 windows, 15205 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1302 | 51.5 | 49.7 | $-178.15 | -1.4% | $821.85 | -0.5 | done | can't tell from luck |
| value_ev20 | 299 | 33.1 | 35.2 | $-344.01 | -11.5% | $655.99 | -1.5 | done | can't tell from luck |
| trend_filter | 887 | 50.7 | 51.0 | $-449.63 | -5.1% | $550.37 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1538 | 49.7 | 49.8 | $-698.38 | -4.5% | $301.62 | -1.8 | done | can't tell from luck |
| value_ev10 | 718 | 36.8 | 39.4 | $-802.00 | -11.2% | $198.00 | -2.5 | done | losing for real |
| value_ev5 | 1069 | 39.2 | 41.2 | $-989.10 | -9.3% | $10.90 | -2.6 | done | losing for real |
| reversal_15m_0.10pct | 1538 | 50.3 | 51.2 | $-1054.47 | -6.9% | $-54.47 | -2.8 | done | losing for real |
| coinflip | 2184 | 49.9 | 50.5 | $-1279.28 | -5.9% | $-279.28 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1302 | 48.5 | 51.2 | $-1357.21 | -10.4% | $-357.21 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2184 | 50.1 | 51.8 | $-1616.28 | -7.4% | $-616.28 | -3.6 | done | losing for real |
| always_up | 2184 | 46.7 | 50.0 | $-2451.03 | -11.2% | $-1451.03 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3441 | 47.4 | 49.2 | $-2856.81 |
| ETH | 3792 | 47.8 | 48.6 | $-2782.49 |
| SOL | 3967 | 47.6 | 48.7 | $-3123.76 |
| XRP | 4005 | 48.4 | 48.6 | $-2456.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
