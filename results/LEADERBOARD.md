# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 9:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1109 windows, 30696 settled trades, 31 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 586 | 34.3 | 35.1 | $-390.56 | -6.7% | $609.44 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3096 | 51.2 | 50.4 | $-779.24 | -2.5% | $220.76 | -1.4 | done | can't tell from luck |
| value_ev10 | 1430 | 37.8 | 39.1 | $-960.15 | -6.7% | $39.85 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2605 | 49.8 | 49.4 | $-1078.51 | -4.1% | $-78.51 | -2.1 | done | losing for real |
| value_ev5 | 2168 | 39.8 | 41.0 | $-1355.13 | -6.3% | $-355.13 | -2.5 | done | losing for real |
| trend_filter | 1817 | 49.3 | 50.4 | $-1362.21 | -7.5% | $-362.21 | -3.3 | done | losing for real |
| coinflip | 4431 | 50.5 | 50.2 | $-1682.26 | -3.8% | $-682.26 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2605 | 50.2 | 51.1 | $-1699.21 | -6.5% | $-699.21 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3096 | 48.8 | 50.2 | $-2130.48 | -6.9% | $-1130.48 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4431 | 50.7 | 51.4 | $-2372.26 | -5.4% | $-1372.26 | -3.7 | done | losing for real |
| always_up | 4431 | 47.5 | 49.3 | $-3586.88 | -8.1% | $-2586.88 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7030 | 48.4 | 49.0 | $-3520.85 |
| ETH | 7605 | 48.1 | 48.4 | $-4634.77 |
| SOL | 7985 | 48.1 | 48.4 | $-4490.08 |
| XRP | 8076 | 48.2 | 48.2 | $-4751.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
