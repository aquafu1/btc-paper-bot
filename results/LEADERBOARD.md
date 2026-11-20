# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 12:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 931 windows, 25724 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1164 | 38.1 | 39.0 | $-662.90 | -5.7% | $337.10 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2627 | 50.9 | 50.6 | $-906.25 | -3.4% | $93.75 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2194 | 50.1 | 49.8 | $-933.02 | -4.3% | $66.98 | -2.0 | done | can't tell from luck |
| trend_filter | 1528 | 49.9 | 51.0 | $-1075.88 | -7.0% | $-75.88 | -2.8 | done | losing for real |
| value_ev5 | 1767 | 39.7 | 41.0 | $-1087.33 | -6.2% | $-87.33 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 2194 | 49.9 | 50.9 | $-1520.40 | -6.9% | $-520.40 | -3.3 | done | losing for real |
| coinflip | 3716 | 50.4 | 50.4 | $-1535.80 | -4.1% | $-535.80 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2627 | 49.1 | 50.3 | $-1647.33 | -6.3% | $-647.33 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3716 | 50.9 | 51.6 | $-1938.16 | -5.2% | $-938.16 | -3.3 | done | losing for real |
| always_up | 3716 | 46.8 | 49.7 | $-3773.60 | -10.2% | $-2773.60 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5861 | 48.1 | 49.1 | $-3435.71 |
| ETH | 6399 | 48.2 | 48.6 | $-4008.56 |
| SOL | 6711 | 48.2 | 48.6 | $-3945.19 |
| XRP | 6753 | 48.3 | 48.5 | $-3836.94 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
