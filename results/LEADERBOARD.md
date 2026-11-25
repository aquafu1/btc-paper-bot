# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 9:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1348 windows, 35356 settled trades, 404 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 698 | 34.1 | 35.4 | $-568.07 | -8.1% | $431.93 | -1.6 | done | can't tell from luck |
| value_ev10 | 1706 | 38.7 | 39.2 | $-844.05 | -4.9% | $155.95 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3537 | 50.8 | 50.1 | $-1049.40 | -3.0% | $-49.40 | -1.8 | done | can't tell from luck |
| value_ev5 | 2574 | 40.4 | 41.1 | $-1351.12 | -5.2% | $-351.12 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2972 | 49.4 | 49.5 | $-1445.27 | -4.9% | $-445.27 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2972 | 50.6 | 50.9 | $-1573.56 | -5.3% | $-573.56 | -2.9 | done | losing for real |
| trend_filter | 2102 | 48.7 | 50.5 | $-1789.16 | -8.5% | $-789.16 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3537 | 49.2 | 50.3 | $-2199.90 | -6.2% | $-1199.90 | -3.7 | done | losing for real |
| coinflip | 5086 | 50.0 | 50.1 | $-2306.43 | -4.5% | $-1306.43 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5086 | 50.3 | 51.4 | $-3036.04 | -6.0% | $-2036.04 | -4.4 | done | losing for real |
| always_up | 5086 | 47.8 | 49.3 | $-3728.22 | -7.3% | $-2728.22 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8682 | 47.8 | 48.8 | $-5321.89 |
| ETH | 9364 | 48.2 | 48.2 | $-4985.11 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
