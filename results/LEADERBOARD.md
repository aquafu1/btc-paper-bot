# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 2:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1370 windows, 35648 settled trades, 420 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 708 | 34.2 | 35.4 | $-559.64 | -7.9% | $440.36 | -1.6 | done | can't tell from luck |
| value_ev10 | 1727 | 38.7 | 39.2 | $-808.68 | -4.7% | $191.32 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3563 | 50.9 | 50.1 | $-993.45 | -2.8% | $6.55 | -1.7 | done | can't tell from luck |
| value_ev5 | 2603 | 40.5 | 41.1 | $-1300.78 | -5.0% | $-300.78 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2988 | 49.3 | 49.4 | $-1475.42 | -4.9% | $-475.42 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2988 | 50.7 | 50.9 | $-1536.13 | -5.1% | $-536.13 | -2.9 | done | losing for real |
| trend_filter | 2118 | 48.6 | 50.4 | $-1853.46 | -8.8% | $-853.46 | -4.1 | done | losing for real |
| coinflip | 5130 | 50.0 | 50.0 | $-2200.64 | -4.3% | $-1200.64 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3563 | 49.1 | 50.2 | $-2227.69 | -6.3% | $-1227.69 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5130 | 50.1 | 51.3 | $-3189.84 | -6.2% | $-2189.84 | -4.6 | done | losing for real |
| always_up | 5130 | 47.8 | 49.3 | $-3723.14 | -7.3% | $-2723.14 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8827 | 47.9 | 48.8 | $-5160.84 |
| ETH | 9511 | 48.1 | 48.1 | $-5123.79 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
