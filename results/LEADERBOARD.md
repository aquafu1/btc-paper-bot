# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 12:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 882 windows, 24376 settled trades, 28 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 460 | 35.7 | 34.9 | $-89.37 | -1.9% | $910.63 | -0.3 | done | can't tell from luck |
| value_ev10 | 1120 | 38.3 | 39.1 | $-587.55 | -5.2% | $412.45 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2064 | 50.0 | 49.7 | $-880.65 | -4.3% | $119.35 | -1.9 | done | can't tell from luck |
| trend_filter | 1434 | 50.3 | 50.9 | $-890.11 | -6.2% | $109.89 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2487 | 50.5 | 50.4 | $-1009.74 | -4.1% | $-9.74 | -2.0 | done | losing for real |
| value_ev5 | 1691 | 39.9 | 41.0 | $-1014.77 | -6.0% | $-14.77 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2487 | 49.5 | 50.4 | $-1372.84 | -5.5% | $-372.84 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2064 | 50.0 | 51.0 | $-1399.43 | -6.8% | $-399.43 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3523 | 51.4 | 51.7 | $-1509.64 | -4.3% | $-509.64 | -2.6 | done | losing for real |
| coinflip | 3523 | 50.2 | 50.3 | $-1564.18 | -4.4% | $-564.18 | -2.7 | done | losing for real |
| always_up | 3523 | 46.9 | 49.6 | $-3441.32 | -9.8% | $-2441.32 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5561 | 48.3 | 49.1 | $-3016.90 |
| ETH | 6067 | 48.2 | 48.5 | $-3722.87 |
| SOL | 6357 | 48.3 | 48.5 | $-3530.18 |
| XRP | 6391 | 48.4 | 48.5 | $-3489.64 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
