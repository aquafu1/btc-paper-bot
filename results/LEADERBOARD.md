# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 10:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1162 windows, 32144 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 620 | 34.7 | 35.3 | $-375.55 | -6.1% | $624.45 | -1.1 | done | can't tell from luck |
| value_ev10 | 1522 | 38.4 | 39.2 | $-823.32 | -5.4% | $176.68 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3222 | 50.8 | 50.4 | $-1083.13 | -3.4% | $-83.13 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2716 | 49.7 | 49.4 | $-1127.64 | -4.2% | $-127.64 | -2.2 | done | losing for real |
| value_ev5 | 2297 | 40.3 | 41.1 | $-1231.12 | -5.4% | $-231.12 | -2.2 | done | losing for real |
| trend_filter | 1903 | 49.0 | 50.5 | $-1512.25 | -7.9% | $-512.25 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2716 | 50.3 | 51.1 | $-1727.30 | -6.4% | $-727.30 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3222 | 49.2 | 50.2 | $-1906.57 | -5.9% | $-906.57 | -3.4 | done | losing for real |
| coinflip | 4642 | 50.2 | 50.2 | $-1990.70 | -4.3% | $-990.70 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 4642 | 50.1 | 51.4 | $-2925.54 | -6.3% | $-1925.54 | -4.4 | done | losing for real |
| always_up | 4642 | 47.8 | 49.3 | $-3436.65 | -7.4% | $-2436.65 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7373 | 48.2 | 49.0 | $-3851.90 |
| ETH | 7973 | 48.2 | 48.4 | $-4635.18 |
| SOL | 8361 | 48.0 | 48.4 | $-4623.90 |
| XRP | 8437 | 48.1 | 48.2 | $-5028.79 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
