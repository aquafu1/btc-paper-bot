# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 3:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1086 windows, 30027 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 564 | 34.6 | 35.2 | $-322.67 | -5.7% | $677.33 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3033 | 51.1 | 50.5 | $-870.27 | -2.9% | $129.73 | -1.6 | done | can't tell from luck |
| value_ev10 | 1389 | 37.8 | 39.2 | $-933.87 | -6.7% | $66.13 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2552 | 49.8 | 49.5 | $-1079.69 | -4.2% | $-79.69 | -2.1 | done | losing for real |
| trend_filter | 1785 | 49.5 | 50.6 | $-1257.27 | -7.0% | $-257.27 | -3.0 | done | losing for real |
| value_ev5 | 2111 | 39.8 | 41.1 | $-1321.61 | -6.3% | $-321.61 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2552 | 50.2 | 51.1 | $-1666.50 | -6.5% | $-666.50 | -3.4 | done | losing for real |
| coinflip | 4336 | 50.5 | 50.3 | $-1671.72 | -3.9% | $-671.72 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3033 | 48.9 | 50.3 | $-2017.95 | -6.7% | $-1017.95 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4336 | 51.0 | 51.5 | $-2088.44 | -4.8% | $-1088.44 | -3.3 | done | losing for real |
| always_up | 4336 | 47.4 | 49.4 | $-3594.20 | -8.3% | $-2594.20 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6853 | 48.5 | 49.0 | $-3369.06 |
| ETH | 7437 | 48.2 | 48.5 | $-4447.27 |
| SOL | 7831 | 48.1 | 48.5 | $-4463.75 |
| XRP | 7906 | 48.3 | 48.3 | $-4544.12 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
