# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 3:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1134 windows, 31326 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 601 | 34.6 | 35.2 | $-363.62 | -6.1% | $636.38 | -1.1 | done | can't tell from luck |
| value_ev10 | 1468 | 38.1 | 39.2 | $-901.13 | -6.1% | $98.87 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3154 | 51.0 | 50.5 | $-905.65 | -2.9% | $94.35 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2644 | 49.7 | 49.4 | $-1137.55 | -4.3% | $-137.55 | -2.2 | done | losing for real |
| value_ev5 | 2221 | 40.1 | 41.1 | $-1283.06 | -5.8% | $-283.06 | -2.3 | done | losing for real |
| trend_filter | 1856 | 49.0 | 50.4 | $-1456.36 | -7.8% | $-456.36 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2644 | 50.3 | 51.1 | $-1657.08 | -6.3% | $-657.08 | -3.3 | done | losing for real |
| coinflip | 4528 | 50.4 | 50.2 | $-1801.36 | -4.0% | $-801.36 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 3154 | 49.0 | 50.2 | $-2023.03 | -6.4% | $-1023.03 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4528 | 50.2 | 51.4 | $-2786.39 | -6.2% | $-1786.39 | -4.3 | done | losing for real |
| always_up | 4528 | 47.8 | 49.3 | $-3400.38 | -7.5% | $-2400.38 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7178 | 48.3 | 49.0 | $-3643.20 |
| ETH | 7761 | 48.2 | 48.4 | $-4596.00 |
| SOL | 8153 | 48.0 | 48.4 | $-4647.30 |
| XRP | 8234 | 48.1 | 48.2 | $-4829.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
