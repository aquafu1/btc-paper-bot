# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 12:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 401 windows, 11002 settled trades, 32 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 199 | 36.7 | 36.5 | $-56.95 | -2.9% | $943.05 | -0.3 | Sun 1:00 AM | too few trades (199/200) |
| value_ev10 | 518 | 40.5 | 40.5 | $-164.41 | -3.2% | $835.59 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 935 | 50.9 | 49.8 | $-180.92 | -1.9% | $819.08 | -0.6 | done | can't tell from luck |
| trend_filter | 625 | 50.2 | 50.6 | $-295.23 | -4.7% | $704.77 | -1.2 | done | can't tell from luck |
| value_ev5 | 778 | 42.0 | 42.2 | $-297.60 | -3.8% | $702.40 | -0.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1106 | 49.6 | 49.8 | $-425.80 | -3.8% | $574.20 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 1106 | 50.4 | 52.0 | $-773.79 | -7.0% | $226.21 | -2.4 | done | losing for real |
| coinflip | 1600 | 50.2 | 50.9 | $-773.81 | -4.8% | $226.19 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 935 | 49.1 | 52.1 | $-884.41 | -9.5% | $115.59 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1600 | 50.0 | 51.6 | $-1040.60 | -6.5% | $-40.60 | -2.7 | done | losing for real |
| always_up | 1600 | 45.9 | 50.8 | $-2077.06 | -13.0% | $-1077.06 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2484 | 47.8 | 49.5 | $-1687.96 |
| ETH | 2766 | 47.9 | 49.0 | $-1698.13 |
| SOL | 2844 | 48.0 | 49.5 | $-2130.64 |
| XRP | 2908 | 48.9 | 49.3 | $-1453.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
