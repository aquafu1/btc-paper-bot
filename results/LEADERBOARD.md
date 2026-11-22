# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 12:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1123 windows, 31074 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 593 | 34.7 | 35.2 | $-335.99 | -5.7% | $664.01 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3133 | 51.2 | 50.5 | $-812.46 | -2.6% | $187.54 | -1.5 | done | can't tell from luck |
| value_ev10 | 1452 | 38.2 | 39.2 | $-861.58 | -5.9% | $138.42 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2634 | 49.7 | 49.4 | $-1108.41 | -4.2% | $-108.41 | -2.2 | done | losing for real |
| value_ev5 | 2197 | 40.1 | 41.1 | $-1223.65 | -5.6% | $-223.65 | -2.2 | done | losing for real |
| trend_filter | 1846 | 49.1 | 50.4 | $-1408.45 | -7.6% | $-408.45 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2634 | 50.3 | 51.1 | $-1674.58 | -6.4% | $-674.58 | -3.3 | done | losing for real |
| coinflip | 4484 | 50.4 | 50.2 | $-1727.58 | -3.9% | $-727.58 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3133 | 48.8 | 50.2 | $-2093.61 | -6.7% | $-1093.61 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4484 | 50.4 | 51.4 | $-2608.66 | -5.8% | $-1608.66 | -4.0 | done | losing for real |
| always_up | 4484 | 47.7 | 49.3 | $-3444.54 | -7.7% | $-2444.54 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7124 | 48.4 | 49.0 | $-3583.87 |
| ETH | 7700 | 48.1 | 48.4 | $-4622.06 |
| SOL | 8085 | 48.1 | 48.4 | $-4468.01 |
| XRP | 8165 | 48.2 | 48.2 | $-4625.57 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
